from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Fruit, Order
from .forms import CheckoutForm
from . import db


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    category = Category.query.order_by(Category.name).all()
    return render_template('index.html', category = category)

@main_bp.route('/fruits/<int:categoryid>/')
def category_fruits(categoryid):
    fruits = Fruit.query.filter(Fruit.category_id==categoryid).all()
    return render_template('fruits.html', fruits = fruits)


@main_bp.route('/fruits/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    fruits = Fruit.query.filter(Fruit.description.like(search)).all()
    return render_template('fruits.html', fruits = fruits)

# Referred to as "Basket" to the user
@main_bp.route('/order/', methods=['POST', 'GET'])
def order():
    fruit_id = request.values.get('fruit_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', surname='', email='', phone='', total_cost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('Failed at creating a new order')
            order = None

    # calculate total price
    totalprice = 0
    if order is not None:
        for fruit in order.fruit:
            totalprice += fruit.price

    # are we adding an item?
    if fruit_id is not None and order is not None:
        fruit = Fruit.query.get(fruit_id)
        if fruit not in order.fruit:
            try:
                order.fruit.append(fruit)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your shopping cart'
            return redirect(url_for('main.order'))
        else:
            flash('Item already in shopping cart')
            return redirect(url_for('main.order'))
    return render_template('order.html', order=order, totalprice=totalprice)


# Delete specific basket items
@main_bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        fruit_to_delete = Fruit.query.get(id)
        try:
            order.fruit.remove(fruit_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# Scrap basket
@main_bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))

    
@main_bp.route('/checkout/', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm() 

    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        if form.validate_on_submit():
           order.status = True
           order.firstname = form.firstname.data
           order.surname = form.surname.data
           order.email = form.email.data
           order.phone = form.phone.data
           order.address = form.address.data
           total_cost = 0
        
           for fruit in order.fruit:
               total_cost = total_cost + fruit.price
           order.total_cost = total_cost
           try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for choosing us! Your order has been confirmed.')
                return redirect(url_for('main.index'))
           except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form)
