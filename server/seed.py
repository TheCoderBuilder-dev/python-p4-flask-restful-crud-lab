from models import db, Plant
from app import app

with app.app_context():
    db.create_all()
    Plant.query.delete()
    db.session.commit()

    seed_data = [
        {"name": "Aloe", "image": "./images/aloe.jpg", "price": 11.50},
        {"name": "Eucalyptus", "image": "./images/eucalyptus.jpg", "price": 9.99},
        {"name": "Monstera", "image": "./images/monstera.jpg", "price": 19.99, "is_in_stock": False}
    ]

    for p in seed_data:
        db.session.add(Plant(**p))
    db.session.commit()
    print(" Seeded DB")
