from flask import Flask, jsonify, request
import requests

from functions import *
from readJson import print_products, count_products
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/test', methods=['GET'])
def hello_world():
    return test()

@app.route('/print', methods=['GET'])
def printing():
    return(print_products())


if __name__ == '__main__':
    app.run(debug=True)


# response = requests.get("http://localhost:5000/test")
# print(response.text)
