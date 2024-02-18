from flask import Flask, jsonify, request, session
from flask_cors import CORS
from searchProduct import *
from addProduct import * 
from countProducts import *
from getFarmer import *
from printPoducts import *
from removeProduct import *
import os
from searchProduct import *
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

app = Flask(__name__)

CORS(app)

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
    if not os.path.exists('APIS/users.json') or os.path.getsize('APIS/users.json') == 0:
     with open('APIS/users.json', 'w') as file:
        file.write('[]')

    data = request.get_json()
    print(data)

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    with open('APIS/users.json', 'r') as file:
        users = json.load(file)

    for user in users:
        if user['username'] == username:
            return jsonify({'error': 'Username already exists'}), 400

    user_data = {
        'username': username,
        'password': password,
        'streaks': 0
    }

    users.append(user_data)

    with open('APIS/users.json', 'w') as file:
        json.dump(users, file, indent=4)

    return jsonify({'message': 'User created successfully'}), 201

json_file_path = 'APIS/users.json'
app.secret_key = 'anisha'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    with open(json_file_path, 'r') as file:
        users = json.load(file)

    user = next((u for u in users if u['username'] == username), None)

    if not user or user['password'] != password:
        return jsonify({'error': 'Invalid username or password'}), 401

    session['username'] = user['username']

    with open('frontend/CurrUser.txt', 'w') as file:
        file.write(username)

    return jsonify({'message': 'Login successful'}), 200

@app.route('/searchProduct', methods=['POST'])
def search_food():
    data = request.get_json()
    food_name = data.get('food_name')
    results = search_product(food_name)
    results = results.to_json()
    return jsonify(results)


@app.route('/buy', methods=['POST'])
def buy_product():
    data = request.json
    productId = data.get('productId')

    with open('CurrUser.txt', 'r') as file:
        username = file.read().strip()
        print(username)

    with open('APIS/users.json', 'r') as file:
        users = json.load(file)

    for user in users:
        if user['username'] == username:
            print("the user who bought it was", username)
            user['streaks'] += 1
            break

    with open('APIS/users.json', 'w') as file:
        json.dump(users, file, indent=4)

    with open('APIS/listings.json', 'r') as f:
        products = json.load(f)

    updated_products = [product for product in products if product['id'] != productId]

    with open('APIS/listings.json', 'w') as f:
        json.dump(updated_products, f, indent=4)

    return jsonify({'message': 'Product purchased successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)


