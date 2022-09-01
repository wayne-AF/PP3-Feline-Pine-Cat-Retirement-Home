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


print("""\

      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)   
                    """)


def get_weight(residents):
    """
    Gets the up-to-date weight of the residents from the user and converts the
    data into floats. Raises ValueError if the input cannot be converted into
    a float. 
    """
    weight_data = []
    print("* * Weight Log Section * *\n")
    print("Update residents' weight here.\n")
    print("The entry should be in kilograms.\n")
    for i in residents:
        while True:
            try:
                weight = float(input(f"Enter {i}'s weight:\n"))
                break
            except ValueError:
                print("That is not a valid entry! Please enter a valid weight.\n")
                
        weight_data.append(weight)

    return weight_data


def update_weight_worksheet(weight_data):
    """
    Updates weight worksheet with weight-data from the get_weight function.
    """
    print("Updating weight spreadsheet...\n")
    weight_worksheet = SHEET.worksheet("weight")
    weight_worksheet.append_row(weight_data)
    print("Thank you for updating everyone's weight!\n")





weight_data = get_weight(residents_list)
update_weight_worksheet(weight_data)