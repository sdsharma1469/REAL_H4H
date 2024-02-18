import pandas as pd

def get_farmer():
    farmer_name = input("Enter the name of the farmer: ")
    matching_farmer = df[df['farmer'] == farmer_name]
    return matching_farmer