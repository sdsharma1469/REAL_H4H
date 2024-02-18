import pandas as pd
import uuid

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    contact = int(input("Enter contact information: "))

    new_product = {
        "id": str(uuid.uuid4()),
        "name": name,
        "price": price,
        "quantity": quantity,
        "contact": contact
    }

    df = pd.read_json('listings.json')

    df = df.append(new_product, ignore_index=True)

    df.to_json('listings.json', orient='records')

def remove_product(inputeduuid):
    df = pd.read_json('listings.json')
    if inputeduuid in df['id'].values:
        df = df[df['id'] != inputeduuid]
        df.to_json('listings.json', orient='records')


def count_products():
    df = pd.read_json('listings.json')
    count = 0
    for index, row in df.iterrows():
        count+=1
    return(count)

def print_products():
    df = pd.read_json('listings.json')
    for index, row in df.iterrows():
        print(f"ID: {row['id']}")
        print(f"Product Name: {row['name']}")
        print(f"Price: {row['price']}")
        print(f"Quantity: {row['quantity']}")
        print(f"Contact Number: {row['contact']}")
    return(df.to_string())


def search_product():
    product_name = input("Enter the name of the product to remove: ")

