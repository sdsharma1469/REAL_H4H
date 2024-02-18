import pandas as pd

def count_products():
    df = pd.read_json('listings.json')
    count = 0
    for index, row in df.iterrows():
        count += 1
    return count