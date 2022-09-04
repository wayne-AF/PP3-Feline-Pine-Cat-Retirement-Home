import gspread
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


residents_list = SHEET.worksheet("details").row_values(1)
residents_ideal_weight = SHEET.worksheet("details").row_values(5)


# def residents():
#     print(residents_list)
#     print(residents_ideal_weight)

# residents()



# print("""\

#       |\      _,,,---,,_
# ZZZzz /,`.-'`'    -.  ;-;;,_
#      |,4-  ) )-,_. ,\ (  `'-'
#     '---''(_/--'  `-'\_)   
#                     """)


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


def update_weight_worksheet(weight):
    """
    Updates weight worksheet with weight-data from the get_weight function.
    """
    print("Updating weight spreadsheet...\n")
    weight_worksheet = SHEET.worksheet("weight")
    weight_worksheet.append_row(weight)
    print("Purrfect! Thank you for updating everyone's weight!\n")


def ideal_weight_range():
    """
    Takes the list of ideal weights and converts them into floats to be used in
    the calculate_food function.
    """

# When I tried to declare this variable inside the calculate_calories function, 
# it kept throwing an error message as "not defined" when passed into the 
# update_calories_worksheet function at the
calories_data = []


def calculate_calories(weight):
    """
    Calculates the residents' Resting Energy Requirements (RER) - the calories
    required - based on their latest weight readings. The general rule is that
    a cat requires 45 calories per kg of bodyweight.
    """
    print("Calculating everyone's RER...\n")
    # calories_data = []
    for i in weight:
        calories = i * 45
        calories_data.append(calories)

    return calories_data


def update_calories_worksheet(calories_data):
    """
    Updates calories worksheet with RER data from the calculate_calories
    function.
    """
    print("Updating RER spreadsheet...\n")
    calories_worksheet = SHEET.worksheet("RER")
    calories_worksheet.append_row(calories_data)
    print("Everyone's RER has been updated!\n")


def calculate_multiplier(weight_data, ideal_weight):
    """
    Compares latest weight data against the ideal weight range and assigns
    the appropriate multiplier based on whether recorded weight is above the
    ideal weight range (weight loss multiplier), above it (weight gain
    multiplier), or with the range (weight maintenance).
    """
    print(weight_data)
    print(residents_ideal_weight)


def weight_management_menu():
    weight_data = get_weight(residents_list)
    update_weight_worksheet(weight_data)
    calculate_calories(weight_data)
    update_calories_worksheet(calories_data)
    calculate_multiplier(weight_data, residents_ideal_weight)


def main():
    """
    Main menu and first page to appear to user. Contains all the options for
    the user to select.
    """
    print("Welcome to the Feline Pine Cat Retirement Home management system.\n")
    print("Please select from the options below.\n")
    print("1. Resident Directory Management\n")
    print("2. Weight Management Menu\n")
    print("3. Food Management Menu")
    print("4. Exit Management System\n")
    
    selection = input("Please make your selection:\n")

    if selection == "1":
        directory_menu()
    elif selection == "2":
        weight_management_menu()
    elif selection == "3":
        food_management_menu()
    elif selection == "4":
        print("Thank you for using the Management System.")
