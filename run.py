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


residents_list = SHEET.worksheet("current residents").col_values(1)
past_residents_list = SHEET.worksheet("past residents").col_values(1)
residents_ideal_weight = SHEET.worksheet("current residents").col_values(5)
new_resident_keys = ["Name:", "Age:", "Sex (M or F):", "Breed:", "Ideal weight (+/- 0.5):", "Medical conditions:"]


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
    Gets the up-to-date weight of the residents from the user and converts
    the data into floats. Raises ValueError if the input cannot be converted
    into a float.
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


# def update_weight_worksheet(weight):
#     """
#     Updates weight worksheet with weight-data from the get_weight function.
#     """
#     print(" Updating weight spreadsheet...\n")
#     weight_worksheet = SHEET.worksheet("weight")
#     weight_worksheet.append_row(weight)
#     print(" Purrfect! Thank you for updating everyone's weight!\n")


# def ideal_weight_range():
#     """
#     Takes the list of ideal weights and converts them into floats to be used in
#     the calculate_food function.
#     """


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


# def update_calories_worksheet(calories_data):
#     """
#     Updates calories worksheet with RER data from the calculate_calories
#     function.
#     """
#     print(" Updating RER spreadsheet...\n")
#     calories_worksheet = SHEET.worksheet("RER")
#     calories_worksheet.append_row(calories_data)
#     print(" Everyone's RER has been updated!\n")


# def convert_weight_range_float(ideal_weight):
    # """
    # Takes the weight range values from the details worksheet and converts
    # them into floats.
    # """
    # print("Retrieving residents' healthy weight range...")
    # ideal_weight_list = [item.split(', ') for item in ideal_weight]
    # ideal_weight_list_flat = [item for i in ideal_weight_list for item in i]
    # ideal_weight_list_flat_float = [float(num) for num in ideal_weight_list_flat]

    # ideal_weight_range = []
    # for i in range(0, len(ideal_weight_list_flat_float), 2):
    #     ideal_weight_range.append((ideal_weight_list_flat_float[i], ideal_weight_list_flat_float[i+1]))
    
    # return ideal_weight_range

def ideal_weight_float(residents_ideal_weight):
    """
    Converts the ideal weight values from the current residents worksheet
    to floats.
    """
    print("converting values to floats")
    ideal_weight_flts = []
    float_weight = [float(i) for i in residents_ideal_weight]
    ideal_weight_flts.append(float_weight)
    
    print("ideal weight floats converted!")

    return ideal_weight_flts


def calculate_calories_multipliers(weight, ideal_weight):
    """
    Compares latest weight data against the ideal weight data and assigns
    the appropriate multiplier based on whether recorded weight is above the
    ideal weight range (weight loss multiplier), below it (weight gain
    multiplier), or within the range (weight maintenance multiplier).
    """
    calorie_multipliers = []
    for i, j in zip(weight, ideal_weight):
        if i < j + 0.5:
            multiplier = 1.8
        elif i > j - 0.5:
            multiplier = 0.8
        else:
            multiplier = 1.2
        calorie_multipliers.append(multiplier)

    print("calorie multipliers calculated")
    return calorie_multipliers


def calculate_calories_required(calories_data, calorie_multipliers):
    """
    Calculates the calories required for each resident.
    """
    print("calculating calories")
    calories_required = []
    for i, j in zip(calories_data, calorie_multipliers):
        calories = i * j
    calories_required.append(calories)
    print("calories_required")
    print("calories calculated!")
    input("testing")
        

def weight_log_menu():
    weight_data = get_weight(residents_list)
    # update_weight_worksheet(weight_data)
    calculate_calories(weight_data)
    # update_calories_worksheet(calories_data)
    # convert_weight_range_float(residents_ideal_weight)
    ideal_weight_float(residents_ideal_weight)
    calculate_calories_multipliers(weight_data, ideal_weight_flts)
    calculate_calories_required(calories_data, calculate_calories_multipliers)


def food_calculator():
    """
    Displays the amount of calories each resident should be getting.
    """




def display_current_residents():
    """
    Creates a dataset with all the residents' data from the details worksheet
    and displays it in a table.
    """
    clear()
    print("Here are all of the current residents.")
    current_residents_worksheet = SHEET.worksheet("current residents")
    current_residents = {
        'age': (current_residents_worksheet.col_values(2)),
        'sex': (current_residents_worksheet.col_values(3)),
        'breed': (current_residents_worksheet.col_values(4)),
        'ideal weight(+/- 0.5)': (current_residents_worksheet.col_values(5)),
        'medical': (current_residents_worksheet.col_values(6))
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
    Creates a dataset with all the data from the past residents worksheet
    and displays it in a table.
    """
    clear()
    print("Here are all of the past residents.")
    past_residents_worksheet = SHEET.worksheet("past residents")
    past_residents = {
        'age': (past_residents_worksheet.col_values(2)),
        'sex': (past_residents_worksheet.col_values(3)),
        'breed': (past_residents_worksheet.col_values(4)),
        'medical': (past_residents_worksheet.col_values(5)),
        'status': (past_residents_worksheet.col_values(6))
    }
    past_residents_data_chart = pd.DataFrame(past_residents, index=[past_residents_list])
    print(past_residents_data_chart)

    selection = input(" Use any key to return to the previous menu.\n")

    if selection:
        directory_menu()
    else:
        pass


def add_new_resident(field):
    """
    Loops through the data fields specified in new_resident_keys list,
    takes input data to create a new resident listing and appends to current
    residents worksheet.
    """
    clear()
    print(" * * Add Resident * * ")
    print(" Enter the new resident's details below.")
    new_resident_details = []
    while True:

        name = input("Name:\n").strip().capitalize()
        if len(name) == 0:
            print("Please enter a valid name.\n")
            continue

        if not isalpha(name):
            print("Please use only letters in the resident's name.")
            continue

        new_resident_details.append(name)
        break

    while True:

        age = input("Age:\n").strip()
        try:
            age = int(age)

        except ValueError:
            print("Please enter a valid age!\n")
            continue

        new_resident_details.append(age)
        break

    while True:

        sex = input("Sex (M/F):\n").strip().upper()
        if sex not in ["M", "F"]:
            print("Please enter M or F.")
            continue
        else:
            new_resident_details.append(sex)
            break

    while True:

        breed = input("Breed:\n").strip().capitalize()
        if len(breed) == 0:
            print("Please provide an entry.\n")
            continue

        if not isalpha(breed):
            print("Please use only letters in the resident's breed.")
            continue

        new_resident_details.append(breed)

        # for i in field:
        #     entry = input(f"{i}\n")
            
        #     new_resident_details.append(entry)

            # return new_resident_details
            
    print(" Thank you for entering the new resident's details. You entered:\n")
    print(new_resident_details)
    print(" If these details are correct, please use 'y' to upload to the directory.\n")
    print(" If you made a mistake, please use 'n' to try again.\n")
    selection = input(" Alternatively, please use 'x' to return to the previous menu.\n")

    if selection == "y":
        update_worksheets_new_resident(new_resident_details)
    elif selection == "n":
        add_new_resident(new_resident_keys)
    elif selection == "x":
        directory_menu()
    else:
        input(" Please select from the options above.\n")


def update_worksheets_new_resident(details):
    """
    Takes the data input by user in add_new_resident function and updates the
    details, weight, food, and RER worksheets.
    """
    print("Updating directory...")
    current_residents_worksheet = SHEET.worksheet("current residents")
    current_residents_worksheet.append_row(details)
    print("Directory updated!\n")
    selection = input(" Use any key to return to the previous menu.\n")

    if selection:
        directory_menu()
    else:
        pass


def remove_resident(list_of_names):
    """
    Removes the selected resident's data from the details, weight, food, and
    RER spreadsheets, and adds the resident's details to the past residents
    spreadsheet. Also asks the user to update the resident's status as deceased
    or adopted.
    """
    clear()
    print("Remove resident\n")
    print(residents_list)
    selection = input("Please enter the name of the resident checking out.\n").strip().capitalize()

    if selection in residents_list:
        confirm = input(f"Do you want to check out {selection}? y/n\n")
        if confirm == "y":
            reason = input("What is the reason for checking out?\n")
        elif confirm == "n":
            input("Please enter the name of the resident checking out.\n")
    else:
        input(f"{selection} is not in the current residents' directory! Please choose from the list of current residents.\n")



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

        if selection == "1":
            display_current_residents()
        elif selection == "2":
            display_past_residents()
        elif selection == "3":
            add_new_resident(new_resident_keys)
        elif selection == "4":
            remove_resident(residents_list)
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
        print(" 3. Food Calculator\n")
        print(" 4. Exit Management System\n")
        
        selection = input(" Please make your selection:\n")

        if selection == "1":
            directory_menu()
        elif selection == "2":
            weight_log_menu()
        elif selection == "3":
            food_calculator()
        elif selection == "4":
            print(" Thank you for using the Feline Pine Management System.\n")
            print(" Have a great day!")
            break
        else:
            input(" Please select from the options above:\n")


main()

# display_past_residents()

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