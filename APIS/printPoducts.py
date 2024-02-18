import pandas as pd
def print_products():
    df = pd.read_json('APIS/listings.json')
    products = []
    for row in df.iterrows():
        product = {
            'id': row[1]['id'],
            'farmer': row[1]['farmer'],
            'name': row[1]['name'],
            'price': row[1]['price'],
            'quantity': row[1]['quantity'],
            'contact': row[1]['contact']
        }
        products.append(product)
    return products
