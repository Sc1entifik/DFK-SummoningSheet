# DFK-SummoningSheet

The purpose of this project is to create a website that will provide you the summoning data for your hero and all the heros you could summon with that hero to get a side by side comparisson to find the best possible summon for that hero as opposed to only being able to see the data for one summon at a time.
While the front end is not built yet the data can be written to .csv spreadsheets to very powerful effect. I

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


Things to come:
- Front end code
	1. Sorting results by stats at the end user level.


