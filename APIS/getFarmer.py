import pandas as pd

def get_farmer(farmer_name):
    df = pd.read_json('APIS/listings.json')
    matching_products = df[df['farmer'] == farmer_name]
    return matching_products

get_farmer('susan')
    