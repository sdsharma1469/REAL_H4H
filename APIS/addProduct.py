import pandas as pd
import uuid

def add_product(name, price, quantity, contact):
    new_product = {

        "id": str(uuid.uuid4()),
        "farmer": str(farmer),
        "name": str(name),
        "price": str(price),
        "quantity": str(quantity),
        "contact": str(contact)
    }

    try:
        df = pd.read_json('APIS/listings.json')
    except FileNotFoundError:
        df = pd.DataFrame(columns=["id", "name", "price", "quantity", "contact"])

    df = df._append(new_product, ignore_index=True)

    df.to_json('APIS/listings.json', orient='records')