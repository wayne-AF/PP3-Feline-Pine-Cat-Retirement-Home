# Feline Pine Cat Retirement Home


[Feline Pine Cat Retirement Home Management System app](https://feline-pine-retirement-home.herokuapp.com/)
## About
The Feline Pine Cat Retirement Home Management System is a command line application for the staff and volunteers at a fictional cat rescue centre. 

It allows users to view current and past cats, add and remove cats, edit their details, input daily weight measurements, and retrieve recommended daily food portions depending on their weight.

The data is stored in and accessed from an external [Google spreadsheet](https://docs.google.com/spreadsheets/d/1lRe6DBT5WJAMoScPgmB7hlruGzHB4QdtOT1pqweaGos/edit?usp=sharing)

## Index - Table of Contents
1. [User Experience](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#user-experience)
	- [User Goals](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#user-goals)
	- [Design and Interface](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#design-and-interface)
2. [Future Features](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#future-features)
3. [Resources](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#resources)
4. [Technologies](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#technologies)
5. [Testing](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#testing)
	- [Validation](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#validation)
	- [Functionality](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#functionality)
	- [Device Compatibility](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#device-compatibility)
	- [Browser Compatibility](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#browser-compatibility)
	- [User Stories](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#user-stories)
6. [Deployment](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#deployment)
	- [Edit and push to repository](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#edit-and-push-code-to-repository)
	- [Configuring APIs](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#create-and-configure-google-spreadsheet-and-apis)
	- [Deploying to Heroku](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#deploying-to-heroku)
[Acknowledgements](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home#acknowledgements)
## User Experience
One of the benefits to using a CLI application at the rescue centre is its simplicity. It requires almost no level of  technological literacy beyond the ability to follow on-screen instructions and type on a keyboard. It is easy to run, requires next to no training, and can be accessed through any browser. 
### User Goals
- To be able to quickly and easily access the management system (MS), possibly while in the middle of carrying out duties with the cats.
- To be able to efficiently use the MS without the need for expansive menus or complicated interfaces.
- To be able to enter new cats into the system, along with the necessary details such as medical conditions.
- To be able to remove cats from the system, i.e. "check out", and have their details saved along with other past cats.
- To be able to update various details about the cats at any time.
- To be able to clearly view all current and past cats.
- To be able to log daily weights for all the cats as many have come from bad backgrounds and may be underweight, overweight, etc. 
- To be able to view the most recent weight logs for all the cats in order to see if they are gaining or losing weight in line with vet recommendations.
- To be able to clearly see the daily recommended food portions all cats should receive dependent on their weight goals.
### Design and Interface
#### General
Menus are clearly laid out and options are clearly titled and numbered so even a user who is not experienced with the MS, or even computer interfaces in general, should be able to navigate and achieve the desired result. The goal was to make every screen easy to read and understand. 

In most menus, even if the user has started a process, e.g. entering a new cat's details, they have the ability to exit out of the process at any stage. 

I changed the HTML background colour of the page to black to make the space feel bigger and less cramped. Button styling and the addition of a title using a font to mimic the font used inside the terminal make the page more cohesive and pleasing to use. 

Throughout, the cats are referred to as "residents" in order to anthropomorphise them in line with the naming of the centre as a retirement home.  
#### Main Menu
The main has a single piece of ASCII artwork to provide the MS some whimsy and make it more visually appealing, and a welcome message to those using it for the first time. The options are clearly labelled and self-explanatory and given adequate spacing to ensure ease of reading. 
![main menu](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/main_menu.png?raw=true)
#### Resident Directory Menu
This menu has the most options of any in the MS but I did not want to make more sub-menus than was necessary. I wanted all actions to be as quick and easy to access as possible. The title of the menu is framed by two asterisks so the user can quickly see which menu they are in. The user is prompted to choose from the options and make a selection. 
![resident directory menu](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/directory_menu.png?raw=true)
* Current Residents Directory
This retrieves the information on all the cats currently in the centre from the Google sheet and clearly lays it out on a chart with pertinent information for the user. A simple enter key press returns the user to the previous menu.
![current residents chart](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/current_residents.png?raw=true)
![current residents google sheet](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/current_res_sheet.png?raw=true)
* Past Residents Directory
This retrieves the information on all the past cats from the Google sheet and clearly lays it out  on a chart. It excludes the ideal weight information and instead has a status field, which is filled in when a cat leaves the home.
![past residents chart](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/past_residents.png?raw=true)

* Add New Resident
Here, the user creates an entry for a new cat. Each data field is clearly labelled. The user can exit out of the process at any time. 
![add res 1](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/add_resident.png?raw=true)
When all information has been entered, the user is asked to confirm and then advised that the directory has been updated. The new cat added to the corresponding Google spreadsheet and is then visible in the Current Residents Directory menu. 
![add res 2](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/add_resident_details.png?raw=true)
The process is simple, intuitive, and clearly laid out. Each entry is validated and if invalid or of an incorrect type, the user is advised of this and asked for a valid input.
![add res 3](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/add_resident_complete.png?raw=true)
* Remove Resident
Here, the user selects which cat to remove from the current directory and asked to select a reason out of three options, before final confirmation if the selection is correct. 
![remove res 1](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/remove_resident.png?raw=true)
![remove res 2](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/remove_resident_details.png?raw=true)
The removed cat is automatically added the past residents Google spreadsheet and is also visible in the Past Residents Directory along with the reason for having left the centre, under the heading of "status". 
![past residents google sheet](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/past_res_sheet.png?raw=true)
* Update Resident Details
The user is able to update specific details of any of the cats currently at the home by selecting their name from a printed list. By numerical selection, the user can choose to edit however many details they wish. Similarly to adding and removing residents, the user is clearly advised they can cancel this process at any time.
![update res details](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/update_resident.png?raw=true)
#### Weight Log Menu
This menu has fewer options than the Resident Directory Menu. Clearly labelled, the user has the option to either update the cats' weight or to view the data from the previous five weigh-ins.
![weight log menu](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/weight_log_menu.png?raw=true)
* Daily Weight Log
The user inputs the cats' latest weight readings here. The MS asks for the weight of the cats one by one in the order in which they appear in the Current Residents Directory. 
![update weight](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/weight_log_details.png?raw=true)
When all weights have been entered, the data is saved to the weight spreadsheet in Google Sheets and the user is advised that the data has been saved. 
![weight google sheet](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/weight_sheet.png?raw=true)
* Recent Weight Data
Data from the last five weigh-ins is retrieved from the weight spreadsheet on Google Sheets and displayed to the user. This allows the user to see if the cats are losing or gaining weight as per their health requirements. 
![recent weight data](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/recent_weight_data.png?raw=true)
#### Daily Food Calculator
This option contains no sub-menus. It compares the cats' most recent weight data, compares it to their ideal weight range, and advises how much food they should be fed.
![daily food](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/daily_food.png?raw=true)

## Future Features
- Ability to directly compare cat's current weight with ideal weight range.
- Recommendations 
- An option for entering required medications and an accompanying function for advising how much and how many times a day to administer
- Short descriptions of each cat for adoption candidates contacting the home
## Resources
- [ASCII Art Archive](https://www.asciiart.eu/animals/cats) - Used for ASCII art
- [Google Fonts](https://fonts.google.com/) - Used to choose and import fonts
- [PEP8 Online](http://pep8online.com/) - Used to validate Python code
- [Pet Place](https://www.petplace.com/article/cats/pet-health/how-to-calculate-your-cats-daily-calorie-intake/) - Used for cat nutritional information
- [StackEdit](https://stackedit.io/) - Used for markdown editing
## Technologies
### Frameworks, Libraries & Programs
- [Git:](https://git-scm.com/) - Used for version control by committing to Git and pushing to GitHub
- [GitHub:](https://github.com/) - Used to store the code pushed from Git
- [Google Auth:](https://google-auth.readthedocs.io/en/master/) - Used Google authentication library for Python to use Google Drive API credentials
- [Google Drive API:](https://developers.google.com/drive/api/v3/about-sdk) - Used to generate credentials to securely access Google Sheets
- [Google Sheets:](https://en.wikipedia.org/wiki/Google_Sheets) - Used to store data on current and past cats and weight logs
- [Google Sheets API:](https://developers.google.com/sheets/api) - Used to enable interactions with Google Sheets
- [gspread:](https://docs.gspread.org/en/latest/) - Used as Python API for Google Sheets
- [Heroku:](https://heroku.com/) - Used to deploy and run the Python application
- [Pandas](https://pandas.pydata.org/) - Used to display data from Google sheets in a DataFrame
## Testing
### Validation
This is the result I received for validating my code with [PEP8 Online](http://pep8online.com/).
![pep8 validation screenshot](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/pep_validation.png?raw=true)
The reported issue relates to the one instance of ASCII artwork featured in the application. Therefore, I am satisfied with the results of the PEP8 validation. 
### Functionality
![pp3_testing_1](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/pp3_testing_1.png?raw=true)
![pp3_testing_2](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/pp3_testing_2.png?raw=true)
![pp3_testing_3](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/pp3_testing_3.png?raw=true)
![pp3_testing_4](https://github.com/wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home/blob/main/documentation/pp3_testing_4.png?raw=true)

### Device Compatibility
As expected, the application was not functional on smartphones or tablets and could only be used on devices that have keyboards in order for application navigation. Tests were conducted on an iMac and a MacBook Air.
### Browser Compatibility
MacOS Monterey v12.5.1:
- Chrome v104.0.5112.101: performed as expected. 
- Firefox v104.0.2: performed as expected. 

MacOS Big Sur v11.6.7:
- Chrome v103.0.5060.113: performed as expected.
- Safari v15.5: performed as expected.
### User Stories
- _I am the owner of Feline Pine. I love cats and taking care of them but I can be a bit disorganised and if I write things down on paper, it tends to get lost. I have no interest in computers so I need an easy way of keeping track of all our residents and some basic details because we can have up to 20 of them living here at the same time!_
	+ If I use the mouse to click the "Run Program" button, the main menu appears. The first option is the Resident Directory Menu. If I enter 1 and press enter, it shows another menu. Here, I can select option 1 for Current Residents Directory. It shows me all the residents we are currently caring for. When I see all the information clearly laid out in front of me like this, I can better organise the chores and tasks that need to be done.
	__Test result: SUCCESS__
- _One of our residents has just been adopted so I need to move them from the current residents list to the past residents list._
	+ From the main menu, I can select the first option again, Resident Directory Menu. The fourth option is Remove Resident. I press 4 and hit enter and it shows me a list of the current residents. The system talks me through the simple and quick process. Once I provide a reason for their departure, the information is saved to the system.
	__Test result: SUCCESS__
- _I am an employee at Feline Pine and am the main party responsible for feeding everyone. Many of the residents are fed different quantities of food and it can be hard to keep track especially because it can change depending on their weight. I need a quick and easy way to check how much I should feed everyone without having to perform any kind of calculations myself._ 
	+ From the main menu of the management system, I can select the third option "Food Calculator". It gives me an easy-to-read, up-to-date calculation of how much food everyone should get, and splits it between a morning and evening meal.
	__Test result: SUCCESS__
- _I am an employee at Feline Pine and am usually the first point of contact for new residents. It is necessary to enter their details into the system as soon as possible but I am not a techie person. I can barely check my email. I need a simple and straightforward method of entering any new resident's details into the system._
	+ From the main menu, I can see the first option is Resident Directory Menu. If I press 1 and enter, the screen takes me to another menu. Here, I can see there are a lot of options but they are quite self-explanatory. The third option is Add New Resident. If I press 3 and enter, the screen changes and it tells me to enter the details for the new resident. The screen is simple and easy to read and understand what to do. I understand how to quit if I suddenly need to do something else. I'm able to enter the details for the new resident quickly and get back to helping them settle in.
	__Test result: SUCCESS__
- _However, sometimes I am in too much of a rush to enter all the details correctly and later on, I realise that I've made a mistake. So I need to be able to go back and change some of the things I've typed._
	+ From the main menu, I go back into Resident Directory Menu. The fifth option is Update Resident Details so I press 5 and hit enter. The screen shows me a list of all the cats we have in the home at the moment and I can type the name of the cat whose details I made a mess of. I don't want to have to enter all the details again but when I follow the instructions on the screen, it shows me the details I typed earlier and I can choose to only change what I have to and easily update the system with the correct information.
	__Test result: SUCCESS__
- _I am a volunteer at Feline Pine a few days a week, and usually help with the daily weight check-ins before feeding time. I want a quick and easy way to input the weight of all the cats without having to navigate complex menus._
	+ From the main menu, I can select the second option for Weight Log Menu. From this menu, I can select the first option for Daily Weight Log and the system asks me for all of the cats' weights one by one and update it to the system.
	__Test result: SUCCESS__
- _I am a vet who volunteers at the home once a week. I'd like to be able to quickly access the recent weight data for all the cats to see if they are gaining or losing weight in line with my recommendations._
	+ From the main menu, I can access the second option for Weight Log Menu and then the second option for Recent Weight Data. All of the current cats' weight data from the last five weigh-ins is visible.
	__Test result: SUCCESS__	
## Deployment
### Edit and push code to repository
#### To clone:
To clone the website's repository to your local computer in order to edit code, add or remove files, and push larger commits, the following steps should be taken:
1. Log into GitHub.
2. Use the search facility or the _Recent Repositories_ list on the left of the screen to locate and select wayne-AF/PP3-Feline-Pine-Cat-Retirement-Home.
3. From the tabs below the menu list and above the file list, click _Code_.
4. There are three methods of creating a clone:
	+ Clone the repository using HTTPS
	+ Clone the repository using an SSH key
	+ Clone the repository using GitHub CLI.
Choose the method and click the button to copy the link. 
5. Open the terminal.
6. Change the current working directory to the desired location for the cloned directory. 
7. Type __git clone__, paste the copied URL, and press _enter_ to create the local clone. 

#### To edit and push:
To edit the website's code and push it to the repository, the following steps should be taken:
1. Log into GitHub.
2. Use the search facility or the _Recent Repositories_ list on the left of the screen, to locate and select wayne-AF/p1-guilguri-tattoo-studio. 
3. From the tabs below the menu list and above the file list, click _Gitpod_.
4. Sign into Gitpod if required. 
5.  Make any desired changes to the code. 
6. In the command line of the terminal, type __git add .__ and hit _enter_.
7. On the next line, type __git commit -m "_enter your commit comment here_"__ and hit _enter_.
8. On the next line, type __git push__ and hit _enter_.
9. Your changes have been pushed to the repository and saved to the project because automatic deployments have been enabled via Heroku for this project.

### Create and configure Google spreadsheet and APIs
#### Create Google spreadsheet:
1. Log into your Google account. 
2. Create a Google spreadsheet and give it a name with the required number of pages, required data fields, etc.
3. In order to share it so that it may be viewed and copied by others with the link, click the Share button in the top right of the window.
4. Under 'General access', change 'Restricted' to 'Anyone with the link'.
5. The link can be copied from the 'Copy link' button and shared with whoever you wish to be able to access the spreadsheet. 
#### Setting up APIs:
1. Navigate to [Google Cloud](https://cloud.google.com/).
2. Create a new project and give it a unique name. Select the project to go to the project page. 
3. Select the APIs & Services from the side menu.
4. Select library. 
5. Search for Google Drive.
6. Select it and click 'enable'.
7. In order to connect to this API, it is necessary to generate credentials. 
8. Click 'Create Credentials' in the top right. 
9. In the form, select 'Google Drive API' from the dropdown menu. 
10. For the data access question, select 'Application Data'.
11. For the question asking if you are planning to use this API with Compute Engine, etc, select 'No, I'm not using them'.
12. Click 'Next'.
13. Enter a Service account name, the click 'Create'.
14. In the Role Dropdown box, choose 'Basic', 'Editor', then 'Continue'.
15. The other options can be left blank. Click 'Done'.
16. On the next page, select the Service Account that you just created.
17. On the next page, select the 'Keys' tab.
18. Click the 'Add Key' dropdown and select 'Create New Key'.
19. Select the JSON and then 'Create'. This will download the JSON file containing the API credentials to your computer.
20. Rename the downloaded file to creds.json. 
21. Copy the creds.json file into the local clone of the project.
22. Make sure the creds.json file is included in the project .gitignore file.
23. In the creds.json file, copy the 'client email' value, and then share with this email address the Google spreadsheet created previously, making sure 'Editor' is selected. 
24. To enable Google Sheets, return to the APIs & Services menu.
25. Select library and search for 'Google Sheets'. 
26. Select it and click 'Enable'.
#### Importing credentials and dependencies:
1. In the terminal of the coding workspace, enter 'pip3 install gspread google-auth'.
2. New dependencies are installed into the workspace. 
3. At the top of the run.py file, type 'import gspread'.
4. Type 'from google.oauth2.service_account import Credentials'.
5. Below this type:
SCOPE = [
"https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"
]
This specifies the APIs that must be accessed.
6. Then type:
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Google spreadsheets name goes here')
### Deploying to Heroku
1. For successful deployment to Heroku, the dependencies information must be added to the requirement.txt file in the project workspace. 
2. In the terminal, type 'pip3 freeze > requirements.txt'. Hitting enter will update the requirements.txt file. Commit and push the changes.
3. Navigate to [Heroku](https://www.heroku.com).
4. Sign in or create an account if necessary. 
5. From the Heroku dashboard, create a new app. 
6. Enter a unique name for the app and select region, then click 'Create App'.
7. On the Application Configuration page for the newly created app, click on the Settings tab and scroll down to the 'Config Vars' section. 
8. Click 'Reveal Config Vars'.
9. In the field for 'Key', type 'CREDS', and then copy the contents of the creds.json file from the project workspace. 
10. Paste into the 'Value' field and click 'Add'.
11. In the next 'Key' field, enter 'PORT', and in the 'Value' field, enter '8000'.
12. Scroll down the Settings page to 'Buildpacks'. 
13. Click 'Add Buildpack', select Python from the menu and save changes.
14. Repeat and add Node.js.
15. Python should be listed first, followed by Node.js.
16. On the Application Configuration page, click on the Deploy tab.
17. Select GitHub as the Deployment Method and confirm.
18. Enter the name of the GitHub repository and click 'Connect'.
19. Scroll down the page and click 'Enable Automatic Deploys' in order to automatically update the app every time changes are push to the GitHub repository. 
20. The application can be run using the 'Open App' button at the top of this page.
## Acknowledgements 
Many thanks to my mentor Brian Macharia for his time and advice!
