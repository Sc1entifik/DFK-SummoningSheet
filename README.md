# DFK-SummoningSheet

The purpose of this project is to create a website that will provide you the summoning data for your hero and all the heros you could summon with that hero to get a side by side comparisson to find the best possible summon for that hero as opposed to only being able to see the data for one summon at a time.
While the front end is not built yet the data can be written to .csv spreadsheets to very powerful effect. I

v0.1:
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

IV commit:
- found and fixed bug in summoning_stat_calculations.py _remaining_stats_step method which caused inaccurate stats when mutation stats would match on both heros on two or more consecutive gene levels
- changed api_pull method in gene_class.py to use id stat instead of normalizedId stat. Which fixed an issue when calling the method with a Crystalvale or Serendale 2.0 prefix added to the hero number



Things to come:
- Front end code
	1. User input forms
	2. Proper .css files to style sheets instead of .css imbeded in html
	3. Sorting results by stats at the end user level.

- Working on showing stats in the order I want without lots and lots of code.
	1. Still working with test file in order to enter all hero queries and get returned all stats to display in an order I would like to see it.


Things that may come:
-methods to write .csv spreadsheets with data if front end takes longer than expected


