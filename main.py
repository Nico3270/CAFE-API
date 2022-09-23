from xml.dom.minidom import Element
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
all_cafes = db.session.query(Cafe).all()
print (all_cafes)   

## HTTP GET - Read Record Randmom
@app.route('/random', methods =["GET"])
def gte_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })

#Extracción de todos los registros
@app.route('/all', methods =["GET"])
def all():
    total_cafes = []
    all_cafes = db.session.query(Cafe).all()
    for random_cafe in all_cafes:
        element = {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    }
        total_cafes.append(element)
    return jsonify(cafes = total_cafes)

## Extracción de un registro según un parametro


@app.route("/search/<direction>")
def search(direction):
    total_locations = []
    locations = Cafe.query.filter_by(location = direction).all()
    for location in locations:
        element = {
        "id": location.id,
        "name": location.name,
        "map_url": location.map_url,
        "img_url": location.img_url,
        "location": location.location,
        "seats": location.seats,
        "has_toilet": location.has_toilet,
        "has_wifi": location.has_wifi,
        "has_sockets": location.has_sockets,
        "can_take_calls": location.can_take_calls,
        "coffee_price": location.coffee_price,
    }
        total_locations.append(element)
    if total_locations == []:
        return jsonify(error = {"Not Found":"Sorry, we don't have a cafe at that location"})
    else:
        return jsonify(cafes = total_locations)


        
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
