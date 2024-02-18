import pandas as pd

def remove_product(inputeduuid):
    df = pd.read_json('APIS/listings.json')
    if inputeduuid in df['id'].values:
        df = df[df['id'] != inputeduuid]
        df.to_json('APIS/listings.json', orient='records')