import pandas as pd
import uuid

import json
import os
import pandas as pd
import uuid

def add_product(name, farmer, price, quantity, contact):
    new_product = {
        "id": str(uuid.uuid4()),
        "name": str(name),
        "farmer": str(farmer),
        "price": str(price),
        "quantity": str(quantity),
        "contact": str(contact)
    }

    file_path = 'APIS/listings.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(new_product)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


    