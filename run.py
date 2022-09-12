import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import pandas as pd
import math
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
recent_weight_data = SHEET.worksheet("weight").row_values


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


def update_weight_worksheet(weight):
    """
    Updates weight worksheet with weight-data from the get_weight function.
    """
    print("Updating weight spreadsheet...\n")
    weight_worksheet = SHEET.worksheet("weight")
    weight_worksheet.append_row(weight)
    print("Purrfect! Thank you for updating everyone's weight!\n")


# When I tried to declare this variable inside the calculate_calories function, 
# it kept throwing an error message as "not defined" when passed into the 
# update_calories_worksheet function at the
calories_data = []


def calculate_calories(weight_data):
    """
    Calculates the residents' Resting Energy Requirements (RER) - the calories
    required - based on their latest weight data. For the purposes of this
    project, I followed the general guideline that a cat requires 45 calories
    per kg of bodyweight.
    """
    print(" Calculating everyone's required calories...\n")
    
    # calories_data = []
    for i in weight_data:
        calories = i * 45
        calories_data.append(calories)

    return calories_data


def get_recent_weight():
    """
    Retrieve values for residents' most recent weight from weight worksheet
    and converts to floats.
    """
    weight_worksheet = SHEET.worksheet("weight").get_all_values()
    recent_weight_data = weight_worksheet[-1]
    print(recent_weight_data)
    recent_weight_floats = [float(i) for i in recent_weight_data]
    
    return recent_weight_floats


def convert_weight_floats(ideal_weight_data):
    """
    Converts the ideal weight values from the current residents worksheet
    to floats.
    """
    print("converting values to floats\n")
    # ideal_weight_floats = []
    ideal_weight_floats = [float(i) for i in ideal_weight_data]
    # ideal_weight_floats.append(float_weight)
    
    print("ideal weight floats converted!\n")
    print(ideal_weight_floats)

    return ideal_weight_floats


def calculate_multipliers(weight, ideal_weight):
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


def calculate_food_required(calorie_data, calorie_multipliers):
    """
    Calculates the calories required for each resident.
    """
    print("calculating calories")
    calories_required = []
    for i, j in zip(calorie_data, calorie_multipliers):
        calories = i * j
        calories_required.append(calories)
    print(calories_required)
    print("calories calculated!")
    return calories_required


def display_food(residents, calories):
    """
    Displays the amount of food in grams each resident should get per meal,
    presuming that 1 gram of food is equal to 1 calorie.
    """
    # clear()
    print("This is the amount of food in grams each resident should get today.\n")
    for i, j in zip(residents, calories):
        print(f"{i}:\n{int(j)} grams -- ({int(math.floor(j / 2))} grams per meal).\n")
        
    selection = input("Use any key to return to the main menu.\n")

    if selection:
        main()
    else:
        pass


def weight_log_menu():
    weight_data = get_weight(residents_list)
    update_weight_worksheet(weight_data)


def food_calculator():
    """
    Displays the amount of calories each resident should be getting.
    """
    recent_weight_floats = get_recent_weight()
    calories_data = calculate_calories(recent_weight_floats)
    ideal_weight_floats = convert_weight_floats(residents_ideal_weight)
    calorie_multipliers = calculate_multipliers(recent_weight_floats, ideal_weight_floats)
    required_calories = calculate_food_required(calories_data, calorie_multipliers)
    display_food(residents_list, required_calories)


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


def add_new_resident():
    """
    Takes input data to create a new resident listing and appends to current
    residents worksheet and weight worksheet.
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

        if not name.isalpha():
            print("Please use only letters in the resident's name.")
            continue

        new_resident_details.append(name)
        break

    while True:

        age = input("Age:\n").strip()
        try:
            age = int(age)

        except ValueError:
            print("Please enter a valid age.\n")
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

        if not breed.isalpha():
            print("Please use only letters in the resident's breed.")
            continue

        else:
            new_resident_details.append(breed)
            break

    while True:
        
        print("Identify the ideal weight range and enter the median figure.\n")
        print("e.g. If ideal weight range is between 4 and 5kg, enter 4.5.\n")

        try:
            ideal_weight = float(input("Ideal weight:\n"))
            
        except ValueError:
            print("Please enter a valid weight.\n")
            continue

        new_resident_details.append(ideal_weight)
        break

    while True:

        medical = input("Medical conditions:\n").strip().capitalize()

        if len(medical) == 0:
            print("Please provide an entry.\n")
            continue

        if not medical.isalpha():
            print("Please provide a valid entry.\n")
            continue

        else:
            new_resident_details.append(medical)
            break
    
    while True:

        try:
            current_weight = float(input("Weight (in kg):\n"))
            break
        except ValueError:
            print("Please enter a valid weight.\n")

        return current_weight

    print("Thank you for entering the new resident's details. You entered:\n")
    print(new_resident_details)
    print("If these details are correct, please use 'y' to upload to the directory.\n")
    print("If you made a mistake, please use 'n' to try again.\n")
    selection = input("Alternatively, please use 'x' to return to the previous menu.\n")

    if selection == "y":
        update_worksheets_new_resident(new_resident_details)
        new_resident_weight_update(current_weight)
    elif selection == "n":
        add_new_resident()
    elif selection == "x":
        directory_menu()
    else:
        input(" Please select from the options above.\n")


def update_worksheets_new_resident(details):
    """
    Takes the data input by user in add_new_resident function and updates the
    current residents and weight worksheets.
    """
    print("Updating directory...\n")
    current_residents_worksheet = SHEET.worksheet("current residents")
    current_residents_worksheet.append_row(details)
    weight_worksheet = SHEET.worksheet("weight")
    res_list_length = len(weight_worksheet.row_values(1))
    weight_worksheet.update_cell(1, (res_list_length + 1), details[0])
    print("Directory updated!\n")
    selection = input("Use any key to return to the previous menu.\n")

    if selection:
        directory_menu()
    else:
        pass


def remove_resident_selection(list_of_names):
    """
    Removes the selected resident's data from the current and weight
    worksheets and adds the data to the past residents worksheet. Also asks
    the user to input a status for the resident, deceased or adopted.
    """
    clear()
    print(" * * Remove resident * *\n")
    print(list_of_names)
    while True:
        selection = input("Please enter the name of the resident checking out or use x to return to previous menu.\n").strip().capitalize()
        
        if selection == "X":
            directory_menu()

        elif selection in list_of_names:
            confirm = input(f"Do you want to check out {selection}? y/n\n")
            if confirm == "x":
                directory_menu()
            elif confirm == "n":
                continue
                # input("Please choose from the list of current residents.\n").strip().capitalize()
            elif confirm == "y":
                reason = input("What is the reason for check out?\n").strip().capitalize()
                print("Adopted, Deceased, Other?\n")
                if reason not in ["Adopted", "Deceased", "Other"]:
                    input("Please provide a valid reason for check out.\n").strip().capitalize()
                    # continue
                else:
                    print(f"Checking out: {selection}\n")
                    print(f"Reason: {reason}\n")
                    proceed = input("Is this correct? y/n or use x to return to previous menu.\n")
                    if proceed == "y":
                        update_worksheets_remove_resident(selection, reason)
                        break
                    elif proceed == "n":
                        continue
                    elif proceed == "x":
                        directory_menu()
                    else:
                        input("Please choose y, n or x.\n")

            else:
                input("Please select y or n or cancel with x.\n")
                continue


def update_worksheets_remove_resident(resident, status):
    """
    Takes the selected resident and selected reason from remove_resident_
    selection function, removes the resident from current residents and
    weight worksheets, and adds to past residents worksheet.
    """
    current_worksheet = SHEET.worksheet("current residents")
    past_worksheet = SHEET.worksheet("past residents")
    weight_worksheet = SHEET.worksheet("weight")
    res_data_remove = current_worksheet.row_values(residents_list.index(resident) + 1)
    current_worksheet.delete_rows(residents_list.index(resident) + 1)
    weight_worksheet.delete_columns(residents_list.index(resident) + 1)
    res_data_remove.pop(4)
    res_data_remove.append(status)
    past_worksheet.append_row(res_data_remove)
    print("Directory updated!\n")
    selection = input("Use any key to return to the main menu.\n")
    if selection:
        main()


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
            add_new_resident()
        elif selection == "4":
            remove_resident_selection(residents_list)
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


# main()
remove_resident_selection(residents_list)

# get_recent_weight()

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