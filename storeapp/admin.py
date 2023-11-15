from flask import Blueprint
from . import db
from .models import Category, Fruit

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():
    category1 = Category(name = 'Berries', image = 'berries.jpg', description = 'The berry fruits are rich in phenolic compounds such as phenolic acids, flavonoids (mainly highly hydroxylated flavonols such as glycosides and other derivatives of quercetin, myricetin, and kaempferol), and anthocyanins.')
    category2 = Category(name = 'Citrus',image = 'citrus.jpg', description = 'Citrus is a genus of flowering plants in the family Rutaceae (orange family) and a common name for edible fruits of this genus (and sometimes related genera). Citrus fruits are a distinctive berry with the internal parts divided into segments and include oranges, lemons, limes, citrons, grapefruit, pomelos (pummelo, pommelo), and mandarins (tangerines). ')
    category3 = Category(name = 'Tropical Fruits', image ='tropicalfruits.jpg', description = 'Tropical fruits are defined as fruits that are grown in hot and humid regions within the Tropic of Cancer and Tropic of Capricorn, covering most of the tropical and subtropical areas of Asia, Africa, Central America, South America, the Caribbean and Oceania.')

    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.commit()
    except:
        return 'There was an issue adding the category in dbseed function'

    
    fruit1 = Fruit(category_id=category1.id, name='Bluberry', image='BLUEBERRIES.png', price=24.99, description='Blueberries are a widely distributed and widespread group of perennial flowering plants with blue or purple berries. They are classified in the section Cyanococcus within the genus Vaccinium. Vaccinium also includes cranberries, bilberries, huckleberries and Madeira blueberries.')
    
    fruit2 = Fruit(category_id=category3.id, name='Banana', image='banana.jpeg', price=6.99, description='Bananas are long, curved fruits with smooth, yellow, and sometimes slightly green skin. The inside of a banana is composed of several fleshy, cream-colored segments, which are surrounded by thin, white membranes. The flesh of the banana is soft, slightly sweet, and has a slightly sticky texture.')
    
    fruit3 = Fruit(category_id=category2.id, name='Orange', image='Orange.jpeg', price=4.99, description='Oranges are small to medium in size, averaging 5-10 centimeters in diameter, and are globular, oblate, or oval in shape. The flesh, depending on the variety, may also contain a few cream-colored seeds. Oranges are aromatic, juicy, and vary in flavor from sweet, acidic, tart, to sour.')
    
    fruit4 = Fruit(category_id=category3.id, name='Mango', image='mango.jpeg', price=2.99, description='Mangoes can have a green, yellow, orange, red or multicoloured skin. The colour of the skin is no indication of the ripeness of the mango. The ripe flesh of the mango is soft and juicy, pale orange in colour, and has a texture ranging from fibrous to almost the consistency of butter.')
    
    fruit5 = Fruit(category_id=category2.id, name='Grapefruit', image='Grapefruit.webp', price=7.99, description='Grapefruit is a citrus fruit with a flavor that can range from bittersweet to sour. It contains a range of essential vitamins and minerals. People can consume the fruit whole or as a juice or pulp. The grapefruit first appeared in the 18th century, as a result of crossing a pomelo and an orange.')
    fruit6 = Fruit(category_id=category1.id, name='Strawberry', image='strawberry.jpeg', price=18.99, description='A strawberry is both a low-growing, flowering plant and also the name of the fruit that it produces. Strawberries are soft, sweet, bright red berries. They are also delicious. Strawberries have tiny edible seeds, which grow all over their surface.')
    
    try:
        db.session.add(fruit1)
        db.session.add(fruit2)
        db.session.add(fruit3)
        db.session.add(fruit4)
        db.session.add(fruit5)
        db.session.add(fruit6)
        db.session.commit()
    except:
        return 'There was an issue adding a fruit in dbseed function'

    return 'DATA LOADED'