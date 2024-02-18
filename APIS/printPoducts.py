import pandas as pd

def print_products():
    df = pd.read_json('APIS/listings.json')
    products = []
    for index, row in df.iterrows():
        product = {
            'id': row['id'],
            'farmer' : row['farmer'],
            'name': row['name'],
            'price': row['price'],
            'quantity': row['quantity'],
            'contact': row['contact']
        }
        products.append(product)
    return products