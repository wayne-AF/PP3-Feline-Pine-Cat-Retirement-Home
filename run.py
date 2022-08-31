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


# def list_residents():
#     details = SHEET.worksheet("details").get_all_values()
#     print(details.columns.values)


# list_residents()

    # new_age = input("Enter new resident's age:\n")
    # new_sex = input("Enter new resident's sex (M or F):\n")
    # new_breed = input("Enter new resident's breed ('unknown' if not known):\n")
    # new_weight = input("Enter new resident's weight in kg:\n")
    # new_healthy_weight = input("Enter new resident's target weight range (upper and lower limit, separated by a comma):\n")



def get_todays_weight():
    """
    The user enters the up-to-date weight of the residents and it is uploaded
    to the weight worksheet.
    """
    print("Enter the residents' weight in the below order.\n")
    print("List of residents goes here.\n")
    print("The readings should be in kilograms, separated by commas.\n")

    weight_data_str = input("Enter today's weight readings:\n")
    print(f"The weight list provided is {weight_data_str}")

get_todays_weight()

