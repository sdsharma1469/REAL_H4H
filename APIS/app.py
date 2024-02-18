from flask import Flask, jsonify, request
from readJson import print_products, count_products, add_product

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/print', methods=['GET'])
def printing():
    return(print_products())

from flask import request

@app.route('/add', methods=['POST'])
def add():
    
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')
    param3 = request.form.get('param3')
    param4 = request.form.get('param4')

    return add_product(param1, param2, param3, param4)



if __name__ == '__main__':
    app.run(debug=True)


# response = requests.get("http://localhost:5000/test")
# print(response.text)
