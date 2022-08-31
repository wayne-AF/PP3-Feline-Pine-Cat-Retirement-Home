import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('feline_pine_cat_retirement_home')


residents_list = ['Bluebell', 'Jafar', 'The Trunchbull', 'Bubbles', 'Artemis']


def get_weight(residents):
    """
    The user enters the up-to-date weight of the residents and validated.
    """
    weight_data = []
    print("Update residents' weight below.\n")
    print("The entry should be in kilograms.\n")
    for i in residents:
        while True:
            try:
                weight = float(input(f"Enter {i}'s weight:\n"))
                break
            except ValueError:
                print("That is not a valid entry. Please enter a valid weight.\n")
                
        weight_data.append(weight)

    return weight_data


get_weight(residents_list)


def update_weight_worksheet():
    """
    Updates weight worksheet with weight-data
    """







 