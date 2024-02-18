import os
import pandas as pd

def print_products():
    # Get the full path to the listings.json file
    json_path = os.path.join(os.path.dirname(__file__), 'listings.json')
    
    # Check if the file exists
    if not os.path.exists(json_path):
        # If the file doesn't exist, return an empty list
        return []

    df = pd.read_json(json_path)
    products = []
    for _, row in df.iterrows():
        product = {
            'id': row.iloc[0],  # Assuming 'id' is the first column
            'farmer': row.iloc[1],  # Assuming 'farmer' is the second column
            'name': row.iloc[2],  # Assuming 'name' is the third column
            'price': row.iloc[3],  # Assuming 'price' is the fourth column
            'quantity': row.iloc[4],  # Assuming 'quantity' is the fifth column
            'contact': row.iloc[5]  # Assuming 'contact' is the sixth column
        }
        products.append(product)
    return products
