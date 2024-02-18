import pandas as pd

df = pd.read_json('APIS/listings.json')

def search_product(name):
    matching_products = df[df['name'] == name]
    return matching_products



