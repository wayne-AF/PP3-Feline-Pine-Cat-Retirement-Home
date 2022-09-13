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

    while True:
        selection = input("Use any key to return to the previous menu.\n")
        if selection:
            weight_log_menu()


def display_recent_weight():
    """
    Displays the most recent weight entries in order to keep track of weight
    gain or weight loss.
    """
    
    weight = SHEET.worksheet("weight")
    # column = weight.col_values(3)
    # print(column)
    # input("do something")
    
    columns = []
    row_length = len(weight.row_values(1)) + 1
    for ind in range(1, row_length):
        column = weight.col_values(ind)
        columns.append(column[-5:])
    # pprint(columns)
    residents = weight.row_values(1)
    for i, j in zip(residents, columns):
        print(f"{i}'s last five weight readings:")
        print(j)
        print()

    selection = input("Use any key to return to the previous menu.\n")
    if selection:
        weight_log_menu()
    else:
        pass
            

def calculate_calories(weight_data):
    """
    Calculates the residents' Resting Energy Requirements (RER) - the calories
    required - based on their latest weight data. For the purposes of this
    project, I followed the general guideline that a cat requires 45 calories
    per kg of bodyweight.
    """
    calories_data = []
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
    recent_weight_floats = [float(i) for i in recent_weight_data]
    
    return recent_weight_floats


def convert_weight_floats(ideal_weight_data):
    """
    Converts the ideal weight values from the current residents worksheet
    to floats.
    """
    ideal_weight_floats = [float(i) for i in ideal_weight_data]

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

    return calorie_multipliers


def calculate_food_required(calorie_data, calorie_multipliers):
    """
    Calculates the calories required for each resident.
    """
    calories_required = []
    for i, j in zip(calorie_data, calorie_multipliers):
        calories = i * j
        calories_required.append(calories)
    
    return calories_required


def display_food(residents, calories):
    """
    Displays the amount of food in grams each resident should get per meal,
    presuming that 1 gram of food is equal to 1 calorie.
    """
    clear()
    print("This is the amount of food each resident should get today.\n")
    for i, j in zip(residents, calories):
        print(f"{i}:\n{int(j)} grams -- ({int(math.floor(j / 2))} grams per meal).\n")
        
    selection = input("Use any key to return to the main menu.\n")

    if selection:
        main()
    else:
        pass


def weight_log_menu():
    """
    Displays the options for the user to select.
    """
    while True:
        clear()
        print(" * * Weight Log Menu * *\n")
        print("Select from the options below.\n")
        print("1. Daily Weight Log\n")
        print("2. Recent Weight Data\n")
        print("3. Return to Main Menu\n")

        selection = input("Please make your selection:\n")

        if selection == "1":
            weight_data = get_weight(residents_list)
            update_weight_worksheet(weight_data)
            # get_weight(residents_list)
        elif selection == "2":
            display_recent_weight()
        elif selection == "3":
            main()
        else:
            input("Please select from the options above:\n")


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
    Creates a dataset with all the residents' data from the current residents
    worksheet and displays it in a table.
    """
    clear()
    print("Here are all of the current residents.")
    current = SHEET.worksheet("current residents")
    res_list = current.col_values(1)
    current_residents = {
        'age': (current.col_values(2)),
        'sex': (current.col_values(3)),
        'breed': (current.col_values(4)),
        'ideal weight(+/- 0.5)': (current.col_values(5)),
        'medical': (current.col_values(6))
    }
    residents_data_chart = pd.DataFrame(current_residents, index=[res_list])
    print(residents_data_chart, "\n")

    selection = input("Use any key to return to the previous menu.\n")

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
    print("Here are all of the past residents.\n")
    past_residents_worksheet = SHEET.worksheet("past residents")
    past_residents = {
        'age': (past_residents_worksheet.col_values(2)),
        'sex': (past_residents_worksheet.col_values(3)),
        'breed': (past_residents_worksheet.col_values(4)),
        'medical': (past_residents_worksheet.col_values(5)),
        'status': (past_residents_worksheet.col_values(6))
    }
    past_residents_data_chart = pd.DataFrame(past_residents, index=[past_residents_list])
    print(past_residents_data_chart, "\n")

    selection = input(" Use any key to return to the previous menu.\n")

    if selection:
        directory_menu()
    else:
        pass


def update_worksheets_new_resident(details, weight):
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
    col_length = len(weight_worksheet.col_values(1))
    weight_worksheet.update_cell(col_length, (res_list_length + 1), weight)
    print("Directory updated!\n")
    selection = input("Use any key to return to the previous menu.\n")

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
    print(" * * Add Resident * *\n")
    print("Enter the new resident's details below.\n")
    new_resident_details = []
    while True:

        name = input("Name:\n").strip().capitalize()
        if len(name) == 0:
            print("Please enter a valid name.\n")
            continue

        if not name.isalpha():
            print("Please use only letters in the resident's name.\n")
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
            print("Please enter M or F.\n")
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
            print("Please use only letters in the resident's breed.\n")
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

        # return current_weight

    print("Thank you for entering the new resident's details. You entered:\n")
    print(new_resident_details, current_weight, "\n")
    print("If these details are correct, please use 'y' to upload to the directory.\n")
    print("If you made a mistake, please use 'n' to try again.\n")
    selection = input("Alternatively, please use 'x' to return to the previous menu.\n")

    if selection == "y":
        update_worksheets_new_resident(new_resident_details, current_weight)
    elif selection == "n":
        add_new_resident()
    elif selection == "x":
        directory_menu()
    else:
        input("Please select from the options above.\n")


def remove_resident_selection():
    """
    Removes the selected resident's data from the current and weight
    worksheets and adds the data to the past residents worksheet. Also asks
    the user to input a status for the resident, deceased or adopted.
    """
    clear()
    current = SHEET.worksheet("current residents")
    res_list = current.col_values(1)
    print(" * * Remove resident * *\n")
    print(res_list, "\n")
    while True:
        selection = input("Please enter the name of the resident checking out or use x to return to previous menu.\n").strip().capitalize()
        
        if selection == "X":
            directory_menu()

        elif selection in res_list:
            confirm = input(f"Do you want to check out {selection}? y/n\n")
            if confirm == "x":
                directory_menu()
            elif confirm == "n":
                continue
                # input("Please choose from the list of current residents.\n").strip().capitalize()
            elif confirm == "y":
                print("What is the reason for check out?\n")
                reason = input("Adopted, Deceased, Other?\n").strip().capitalize()
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
                input("Please select y/n or cancel with x.\n")
                # continue


def update_worksheets_remove_resident(resident, status):
    """
    Takes the selected resident and selected reason from remove_resident_
    selection function, removes the resident from current residents and
    weight worksheets, and adds to past residents worksheet.
    """
    # res_list = current.col_values(1)
    current = SHEET.worksheet("current residents")
    past = SHEET.worksheet("past residents")
    weight = SHEET.worksheet("weight")
    res_data_remove = current.row_values(residents_list.index(resident) + 1)
    current.delete_rows(residents_list.index(resident) + 1)
    weight.delete_columns(residents_list.index(resident) + 1)
    res_data_remove.pop(4)
    res_data_remove.append(status)
    past.append_row(res_data_remove)
    print("Directory updated!\n")
    while True:
        selection = input("Use any key to return to the main menu.\n")
        if selection:
            main()
        else:
            pass


def update_resident_selection(residents):
    """
    Allows the user to select the resident whose details they wish to update.
    """
    clear()
    print(" * * Update Resident Details * *\n")
    print(residents, "\n")
    while True:
        selection = input("Please enter the name of the resident to update or use x to return to previous menu.\n").strip().capitalize()

        if selection == "X":
            directory_menu()

        elif selection in residents:
            confirm = input(f"Do you want to update {selection}'s details? y/n\n")
            if confirm == "x":
                directory_menu()
            elif confirm == "n":
                continue
            elif confirm == "y":
                update_resident_details(selection)
                break
            else:
                input("Please select y/n or cancel with x.\n")


def update_resident_details(resident):
    """
    Allows the user to update the details of the resident selected in the
    update_resident_selection function.
    """
    clear()
    weight = SHEET.worksheet("weight")
    current = SHEET.worksheet("current residents")
    row_index = residents_list.index(resident) + 1
    row_values = current.row_values(residents_list.index(resident) +1)
    details = ["name:", "age:", "sex:", "breed:", "ideal weight:", "medical:"]
    for i, j in zip(details, row_values):
        print(i, j)
    print()
    print("Please only use this menu to provide updated information for a resident.\n")
    print("Do not use it to create a new resident.\n")
    print("Enter 1 to change name.")
    print("Enter 2 to change age.")
    print("Enter 3 to change sex.")
    print("Enter 4 to change breed.")
    print("Enter 5 to change ideal weight.")
    print("Enter 6 to change medical.\n")

    while True:
        selection = input("Please select which details you want to change or x to cancel:\n").strip()

        if selection == "x":
            update_resident_selection(residents_list)
        elif selection == "1":
            name = input("Edit name:\n").strip().capitalize()
            if len(name) == 0:
                print("Please enter a valid name.\n")
                continue
            if not name.isalpha():
                print("Please use only letters in the resident's name.\n")
                continue
            if name in residents_list:
                print("That name is already taken. Please use a new name or new spelling.\n")
                continue
            
            current.update_cell(row_index, 1, name)
            weight.update_cell(1, row_index, name)
            print("Name updated.\n")

        elif selection == "2":
            age = input("Edit age:\n").strip()
            try: 
                age = int(age)
            except ValueError:
                print("Please enter a valid age.\n")
                continue
            
            current.update_cell(row_index, 2, age)
            print("Age updated.\n")

        elif selection == "3":
            sex = input("Edit sex (M/F):\n").strip().upper()
            if sex not in ["M", "F"]:
                print("Please enter M or F.\n")
                continue

            current.update_cell(row_index, 3, sex)
            print("Sex updated.\n")

        elif selection == "4":
            breed = input("Edit breed:\n").strip().capitalize()
            if len(breed) == 0:
                print("Please provide an entry.\n")
                continue
            if not breed.isalpha():
                print("Please use only letters in the resident's breed.\n")
                continue
            
            current.update_cell(row_index, 4, breed)
            print("Breed updated.\n")

        elif selection == "5":
            try:
                ideal_weight = float(input("Edit ideal weight:\n"))
            except ValueError:
                print("Please enter a valid weight.\n")
                continue

            current.update_cell(row_index, 5, ideal_weight)
            print("Ideal weight updated.\n")

        elif selection == "6":
            while True:
                medical = input("Edit medical conditions:\n").strip().capitalize()
                if medical == "x":
                    break
                if len(medical) == 0:
                    print("Please provide an entry.\n")
                    continue
                if not medical.isalpha():
                    print("Please provide a valid entry.\n")
                    continue
                else:
                    current.update_cell(row_index, 6, medical)
                    print("Medical updated.\n")
                    break


def directory_menu():
    """
    Displays all options in the Resident Directory sub-menu.
    """
    while True:
        clear()
        print("* * Resident Directory Menu * *\n")
        print("Please select from the options below.\n")
        print("1. Current Residents Directory\n")
        print("2. Past Residents Directory\n")
        print("3. Add New Resident\n")
        print("4. Remove Resident\n")
        print("5. Update Resident Details\n")
        print("6. Return to Main Menu\n")

        selection = input("Please make your selection:\n")

        if selection == "1":
            display_current_residents()
        elif selection == "2":
            display_past_residents()
        elif selection == "3":
            add_new_resident()
        elif selection == "4":
            remove_resident_selection()
        elif selection == "5":
            update_resident_selection(residents_list)
        elif selection == "6":
            main()
        else:
            input("Please select from the options above:\n")
            continue


def main():
    """
    Main menu and first page to appear to user. Contains all the options for
    the user to select.
    """
    while True:
        clear()
        print(" * * Feline Pine Cat Retirement Home * *")
        print("""\

        |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
        |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)   
                        """)
    
        print("Welcome to the Feline Pine management system.\n")
        print("Please select from the options below.\n")
        print("1. Resident Directory Management\n")
        print("2. Weight Log Menu\n")
        print("3. Food Calculator\n")
        print("4. Exit Management System\n")
        
        selection = input("Please make your selection:\n")

        if selection == "1":
            directory_menu()
        elif selection == "2":
            weight_log_menu()
        elif selection == "3":
            food_calculator()
        elif selection == "4":
            print("Thank you for using the Feline Pine Management System.\n")
            print("Have a great day!")
            break
        else:
            input("Please select from the options above:\n")
            continue


# update_resident_selection(residents_list)
main()
# remove_resident_selection()
# weight_log_menu()
# display_recent_weight()

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