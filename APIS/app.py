from flask import Flask, jsonify, request
from readJson import print_products, count_products, add_product

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/print', methods=['GET'])
def printing():
    return print_products()

@app.route('/add', methods=['POST'])
def add():
    data = request.json  # Assuming the data is sent as JSON
    param1 = data.get('productName')
    param2 = data.get('productPrice')
    param3 = data.get('productQuantity')
    param4 = data.get('productContact')  # Corrected the parameter name
    # Assuming add_product takes four parameters
    add_product(param1, param2, param3, param4)
    return jsonify({'message': 'Product added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
