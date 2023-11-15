from . import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        str = "ID: {}, Name: {}, Description: {}, Image: {} \n" 
        str = str.format(self.id, self.name, self.description, self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('fruit_id',db.Integer,db.ForeignKey('fruits.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'fruit_id') )

class Fruit(db.Model):
    __tablename__ = 'fruits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    
    def __repr__(self):
        str = "ID: {}, Name: {}, Description: {}, Image: {}, Price: {}, Category: {}\n" 
        str = str.format(self.id, self.name, self.description, self.image, self.price, self.category_id)
        return str

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(200))
    fruit = db.relationship("Fruit", secondary=orderdetails, backref="orders")
    total_cost = db.Column(db.Float)
    
    def __repr__(self):
        str = "ID: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Address: {}, Fruit: {}, Total Cost: {}\n" 
        str = str.format(self.id, self.status, self.firstname, self.surname, self.email, self.phone, self.address, self.fruit, self.total_cost)
        return str