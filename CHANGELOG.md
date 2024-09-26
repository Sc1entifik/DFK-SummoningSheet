v-0.1:
- README.md
- Functional back end that can retrieve data needed from the api
1. summoning_stat_calculations.py
2. gene_class.py


v-0.2:
- changed gene_type_list to a class variable from an instance variable for clearer readability and to better fit DRY principle
- added stats_genes_dictionary and visual_genes_dictionary which returns all translated genes data into a nice dictionary
- fixed issue when calling _inital_stats_steps for visual genes


v-0.3:
- fixed issue with summoning_stat_calculations not working when being imported from another .py file
- started on front end:
	1. Created flask app controller file named app.py
	2. Created html files for app.py to render and started styling those files 


v-0.4:
- found and fixed bug in summoning_stat_calculations.py _remaining_stats_step method which caused inaccurate stats when mutation stats would match on both heros on two or more consecutive gene levels
- changed api_pull method in gene_class.py to use id stat instead of normalizedId stat. This fixed an issue when calling the method with a Crystalvale or Serendale 2.0 prefix added to the hero number


v-0.5:
- Created front end logic for a dynamic webpage which changes stat order appearance in accordance with the best profession and classes to pass
- Added new getter functions and variables in SummonStatistics class.
- Created an inner function and ternary statement to handle CV and SD2.0 hero numbers

v-0.55
- Added a form for gathering hero data from user input and created a class for handling that data and returning it to the controller in app.py
	1. Created form.py
	2. Created hero_form.html
- Modified inner function hero_number_prefix inside of start_sheet function in app.py to be callable while passing the your_hero variable to it as well as being able to make a map object with the hero_candidate lists.
- Modified start_sheet in app.py to get the your_hero, cv_candidates_list, sd_candidate_list, and sd_2candidate_list to accept user inputs from web forms instead of preset values.

v-0.75
- Added input forms on hero_form.html for summoning costs.
- Added rarity odds data for summoned heroes.
- Found and fixed bug which caused most purple stat data to return 0.
- Made small improvements to headers to be displayed by start_sheet.html
- Removed unnecessary lines of code found in gene_class.py
- Cleaned up app.py making it easier to read and easier to maintain.
- Added controller class to handle data and prepare it for display.
	1. Created controller.py

v-0.78
- Styled website with css styling sheet.
- Added Medieval style font to match website theme

v-1.0
- Finished styling website
- Added error handling for web forms filled out incorrectly.

v-1.1
- Made changes to no longer commit venv files after finding out they were not necessary
- Added Dockerfile to create a Docker image file for easier deployment.
- Found and fixed bug causing an error when looking up Legionnaire heroes.

v-1.25
- Found and fixed bug when searching for heroes with the Fishing profession

v-1.30
- Found and fixed bug when searching for Berserker class heroes

v-1.32
- Added module for getting mat data from dexscreener api.
- Built test for dexscreener api module.
- Updated requirements.txt for project to work with python 3.12.

v-1.4
- Refactored dexscreener api to be split into an Enum style main class, an initializer sub class, and a database manager subclass.
- Refactored _return_updated_database_dictionary to use decorators.
- Found out why the key:value pairs were sometimes mismatching and fixed it.
- Revamped json database to hold all relevent data for project

v-1.6
- Created method which determines if it is time to update the materials database
- Added missing mats to mats lists in dexscreener_api.py
- Removed duplicate mats to mats lists in dexscreener_api.py
- Built tests for dexscreener_api.py module

v-1.62
- Broke up css files for better modularity and readability.
- Changed most css unit values to relative values.
- Improved front end aestetics.
- Used calc function with footer for better placement with relative positioning instead of absolute.

v-1.621
- Discovered bug rarely giving strange hero summons odds.
- Refactored some code
- Renamed variables
- Removed an unneccesary variables from summoning_stat_calculations.py
- Added comment for extra clarity.


v-1.63
- Found and fixed bug.
- Bug only triggered rarely when dominant and recessive 3 genes triggered on both heroes at the same time. This was due to a block changing the index value to -1 which would call the recessive_3 gene which is an unwanted behavior
- Changed boolean to not trigger the code block if the index value is zero which is the index for dominant.
- Changed the name of stats_genes_dictionary in summoning_stat_calculations.py to summon_stats_genetics_dictionary

v-1.7
- Changed form to take hero costs inside the same input as the hero numbers for a cleaner looking user input experience.
- Modified controller.py module to obtain data from the new forms.


v-1.8
- Removed all table row and header methods from controller.py
- Modified controller.py to return a dictionary for filling out the end Summoner Sheet page instead of table and header lists
- Small refactors on gene_class.py, controller.py, and summoning_stat_calculations.py for cleaner and more maintainable code.
- Renamed start_sheet.html to summon_sheet.html.
- Revamped summon_sheet.html to display data with a .css grid instead of a table layout.
- Huge modifications to summon_sheet.css to reflect new grid layout.


v-1.9
- Changed CSS for Summoning Sheet part of app.
- Added media queries.
- Added _stats_subheader_dictionary to controller.py to change stats layout.

v-1.95
- Built controller for the mats-profitability form to get the profitability data from the dexscreener api.
- Created media queries to make mats input form look good on any device.
- Made random improvements to codebase.
- Built mining_results.html
- Built mining_results.css
- Built media_mining_results.css

v-1.952
- Created media quearies for mining_results.html
- Minor tweaks to mining_results.html and mining_results.css including p tag color change.


v-2.0
- Created instructions page for Summoner Sheet portion of website.

v-2.001 
- Fixed bug with route name change which caused mats results not to load.

v-2.002
- Put error message on failure form for easier troubleshooting.

v-2.1
- Finished material mining instructions page.
- Removed pictures that were no longer used.
- Added reminder in README.md to set database location on production server.


Things I'm working on for future updates / pseudo coding:
- Build the instructions page for the material mining profitability tool.
- Fix bug where whitespace is not trimmed from entry forms.
- Writing some tests so project remains scalable.
