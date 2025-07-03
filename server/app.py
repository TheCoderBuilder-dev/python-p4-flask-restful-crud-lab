from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Plant
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/plants/<int:id>', methods=['GET', 'PATCH'])
def handle_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    if request.method == 'GET':
        return jsonify({
            "id": plant.id,
            "name": plant.name,
            "image": plant.image,
            "price": plant.price,
            "is_in_stock": plant.is_in_stock
        }), 200

    elif request.method == 'PATCH':
        data = request.get_json()
        if "is_in_stock" in data:
            plant.is_in_stock = data["is_in_stock"]
            db.session.commit()
        return jsonify({
            "id": plant.id,
            "name": plant.name,
            "image": plant.image,
            "price": plant.price,
            "is_in_stock": plant.is_in_stock
        }), 200

@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    db.session.delete(plant)
    db.session.commit()
    return '', 204
