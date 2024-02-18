import pandas as pd


def search_product():
    product_name = input("Enter the name of the product to remove: ")
    matching_products = df[df['name'] == product_name]
    return matching_products
