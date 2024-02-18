from flask import Flask, jsonify, request
from flask_cors import CORS
from searchProduct import *
from addProduct import * 
from countProducts import *
from getFarmer import *
from printPoducts import *
from removeProduct import *


from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import uuid


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/print', methods=['GET'])
def print_data():
    products = print_products()
    return jsonify(products)


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    productName = data.get('productName')
    productFarmerName = data.get('productFarmerName')
    productPrice = data.get('productPrice')
    productQuantity = data.get('productQuantity')
    productContact = data.get('productContact')
    
    print(productQuantity)
    add_product(productName, productFarmerName, productPrice, productQuantity, productContact)
    return "Parameters received"


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return "user alr exists"

    new_user = User(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201




if __name__ == '__main__':
    app.run(debug=True)


