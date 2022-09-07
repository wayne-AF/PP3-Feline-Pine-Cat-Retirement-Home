import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import pandas as pd
import numpy as np

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
new_resident_keys = ["Name:", "Age:", "Sex (M or F):", "Breed:", "Ideal weight range (two numbers separated by a comma):"]


# def residents():
#     print(residents_list)
#     print(residents_ideal_weight)

# residents()

def clear():
    """
    Clears screen
    """
    print('\033c')


def get_weight(residents):
    """
    Gets the up-to-date weight of the residents from the user and converts the
    data into floats. Raises ValueError if the input cannot be converted into
    a float.
    """
    clear()
    weight_data = []
    print(" * * Weight Log Section * *\n")
    print(" Update residents' weight here.\n")
    print(" The entry should be in kilograms.\n")
    for i in residents:
        while True:
            try:
                weight = float(input(f" Enter {i}'s weight:\n"))
                break
            except ValueError:
                print(" That is not a valid entry! Please enter a valid weight.\n")

        weight_data.append(weight)

    return weight_data


def update_weight_worksheet(weight):
    """
    Updates weight worksheet with weight-data from the get_weight function.
    """
    print(" Updating weight spreadsheet...\n")
    weight_worksheet = SHEET.worksheet("weight")
    weight_worksheet.append_row(weight)
    print(" Purrfect! Thank you for updating everyone's weight!\n")


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
    print(" Calculating everyone's RER...\n")
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
    print(" Updating RER spreadsheet...\n")
    calories_worksheet = SHEET.worksheet("RER")
    calories_worksheet.append_row(calories_data)
    print(" Everyone's RER has been updated!\n")


def convert_weight_range_float(ideal_weight):
    """
    Takes the weight range values from the details worksheet and converts
    them into floats.
    """
    print("Retrieving residents' healthy weight range...")
    ideal_weight_list = [item.split(', ') for item in ideal_weight]
    ideal_weight_list_flat = [item for i in ideal_weight_list for item in i]
    ideal_weight_list_flat_float = [float(num) for num in ideal_weight_list_flat]

    ideal_weight_range = []
    for i in range(0, len(ideal_weight_list_flat_float), 2):
        ideal_weight_range.append((ideal_weight_list_flat_float[i], ideal_weight_list_flat_float[i+1]))
    
    return ideal_weight_range


def calculate_multiplier(weight_data, ideal_weight):
    """
    Compares latest weight data against the ideal weight range and assigns
    the appropriate multiplier based on whether recorded weight is above the
    ideal weight range (weight loss multiplier), below it (weight gain
    multiplier), or within the range (weight maintenance multiplier).
    """
    calorie_multipliers = []
    for i, j in zip(weight_data, ideal_weight):
        for num in range(j[0], j[1]):
            if i < j[0]:
                multiplier = 1.8
            elif i > j[1]:
                multiplier = 0.8
            else:
                multiplier = 1.2
            calorie_multipliers.append(multiplier)

        print(calorie_multipliers)
        input("testing")

    
    
    
    #     if i < j:
    #         multiplier = 1.8
    #     elif i > j:
    #         multiplier = 0.8
    #     else:
    #         multiplier = 1.2
    #     calorie_multipliers.append(multiplier)
    # print(calorie_multipliers)
    # input("testing")



#          j in weight_range:
# #             if i < j-0.5:
# #                 print("multiplier is 1.8")
# #             elif i > j+0.5:
# #                 print("multiplier is 0.8")
# #             else:
# #                 print("multiplier is 1.2")
    
    
#     print(weight_data)
#     print(residents_ideal_weight)


def weight_log_menu():
    weight_data = get_weight(residents_list)
    update_weight_worksheet(weight_data)
    calculate_calories(weight_data)
    update_calories_worksheet(calories_data)
    convert_weight_range_float(residents_ideal_weight)
    calculate_multiplier(weight_data, ideal_weight_range)


def display_current_residents():
    """
    Creates a dataset with all the residents' data from the details worksheet
    and displays it in a table.
    """
    clear()
    print("Here are all of the current residents.")
    details_worksheet = SHEET.worksheet("details")
    current_residents = {
        'age': (details_worksheet.row_values(2)),
        'sex': (details_worksheet.row_values(3)),
        'breed': (details_worksheet.row_values(4))
    }
    residents_data_chart = pd.DataFrame(current_residents, index=[residents_list])
    print(residents_data_chart)

    selection = input(" Use any key to return to the previous menu.\n")

    if selection:
        directory_menu()
    else:
        pass
        

def display_past_residents():
    """
    Creates a dataset with all the data from the past_residents worksheet
    and displays it in a table.
    """


def add_new_resident(field):
    """
    Loops through the data fields specified in new_resident_keys list, 
    takes input data to create a new resident listing and appends to details
    worksheet.
    """
    
    while True:
        clear()
        new_resident_details = []
        print(" Enter the new resident's details below.")
        
        for i in field:
            entry = input(f"{i}\n")
            
            new_resident_details.append(entry)

            # return new_resident_details
            
        print(" Thank you for entering the new resident's details. You entered:\n")
        print(new_resident_details)
        print(" If these details are correct, please use '5' to upload to the directory.\n")
        print(" If you made a mistake, please use 'n' to try again.\n")
        selection = input(" Alternatively, please use 'x' to return to the previous menu.\n")

        if selection == "5":
            update_worksheets_new_resident(new_resident_details)
        elif selection == "n":
            add_new_resident(new_resident_keys)
        elif selection == "x":
            directory_menu()
        else:
            input(" Please select from the options above.")


def update_worksheets_new_resident(details):
    """
    Takes the data input by user in add_new_resident function and updates the
    details, weight, food, and RER worksheets.
    """
    print("Updating worksheets...")
    details_worksheet = SHEET.worksheet("details")
    details_worksheet.append_col(details)
    input("waiting")


def remove_resident():
    """
    Removes the selected resident's data from the details, weight, food, and
    RER spreadsheets, and adds the resident's details to the past_residents
    spreadsheet.
    """


def directory_menu():
    """
    Displays all options in the Resident Directory sub-menu.
    """
    while True:
        clear()
        print(" * * Resident Directory Menu * *\n")
        print(" Please select from the options below.\n")
        print(" 1. Current Residents Directory\n")
        print(" 2. Past Residents Directory\n")
        print(" 3. Add New Resident\n")
        print(" 4. Remove Resident\n")
        print(" 5. Return to Main Menu\n")

        selection = input(" Please make your selection:\n")

        if selection == "0":
            print("nope")
        elif selection == "1":  
            display_current_residents()
        elif selection == "2":
            display_past_residents()
        elif selection == "3":
            add_new_resident(new_resident_keys)
        elif selection == "4":
            remove_resident()
        elif selection == "5":
            main()
        else:
            input(" Please select from the options above:\n")


def main():
    """
    Main menu and first page to appear to user. Contains all the options for
    the user to select.
    """
    while True:
        clear()
        print(" Feline Pine Cat Retirement Home")
        print("""\

        |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
        |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)   
                        """)
    
        print(" Welcome to the Feline Pine management system.\n")
        print(" Please select from the options below.\n")
        print(" 1. Resident Directory Management\n")
        print(" 2. Weight Log Menu\n")
        print(" 3. Food Management Menu\n")
        print(" 4. Exit Management System\n")
        
        selection = input(" Please make your selection:\n")

        if selection == "1":
            directory_menu()
        elif selection == "2":
            weight_log_menu()
        elif selection == "3":
            food_management_menu()
        elif selection == "4":
            print(" Thank you for using the Feline Pine Management System.\n")
            print(" Have a great day!")
            break
        else:
            input(" Please select from the options above:\n")


main()


# while True:
#         clear()
#         print("These are all of the current residents.\n")
#         details_worksheet = SHEET.worksheet("details")
#         all_res_dict = np.array(details_worksheet.get_all_values())
        
#         print(all_res_dict)
#         (print("Use 'x' to return to the previous menu.\n"))
#         selection = input("Use 'm' to return to the main menu.\n")

#         if selection == "x":
#             directory_menu()
#         elif selection == "m":
#             main()
#         else:
#             input(" Please select from the options above.\n")