from flask import Flask, jsonify, request
from flask_cors import CORS
from searchProduct import *
from addProduct import * 
from countProducts import *
from getFarmer import *
from printPoducts import *
from removeProduct import *


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
    productPrice = data.get('productPrice')
    productQuantity = data.get('productQuantity')
    productContact = data.get('productContact')
    
    print(productQuantity)
    add_product(productName, productPrice, productQuantity, productContact)
    return "Parameters received"


if __name__ == '__main__':
    app.run(debug=True)


