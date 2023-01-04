# DFK-SummoningSheet

The purpose of this project is to create a website that will provide you the summoning data for your hero and all the heros you could summon with that hero to get a side by side comparisson to find the best possible summon for that hero as opposed to only being able to see the data for one summon at a time.
While the front end is not built yet the data can be written to .csv spreadsheets to very powerful effect. I

In the first commit:
- README.md
- Functional back end that can retrieve data needed from the api
1. summoning_stat_calculations.py
2. gene_class.py


In the second commit:
- changed gene_type_list to a global variable for clearer readability and to better fit DRY principle
- added stats_genes_dictionary and visual_genes_dictionary which returns all translated genes data into a nice dictionary
- fixed issue when calling _inital_stats_steps for visual genes


In the third commit:
- fixed issue with summoning_stat_calculations not working when being imported from another .py file
- started on front end:
	1. Created flask app controller file named app.py
	2. Created html files for app.py to render and started styling those files 

Things to come:
- Front end code
	1. User input forms
	2. Proper .css files to style sheets instead of .css imbeded in html
	3. Sorting results by stats at the end user level.


Things that may come:
-methods to write .csv spreadsheets with data if front end takes longer than expected


