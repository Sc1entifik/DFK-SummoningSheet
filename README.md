# DFK-Summoning Sheet And DFK-Mining Profitability Tool
This project contains the DFK-Summoning Sheet and DFK-Mining Profitability Tool in one website at [https://scientifik.pythonanywhere.com/](https://scientifik.pythonanywhere.com/) since they go together like peanut butter and jelly. These are tools to be used with the [Defi Kingdoms web3 crypto game.](https://defikingdoms.com/)

## Motivation
### DFK-Summoning Sheet 
The purpose of this project was to create a website that would show you all the relevant data for summoning pairs given a hero and multiple summoning candidates with an appealing output using the Defi Kingdoms API. I was frustrated with other projects that show data in unwieldly formats and are hard to parse through or had very little information. This project started as a web scraper which scraped one of these sites multiple times checking one hero against a list of heros and generated a .csv file which allowed me to quickly compare my hero against a list of possible summoning candidates instead of one pair at a time. I was so happy with my results I decided to get my data straight from the Defi Kingdoms API, create this website, and share it with everyone.

### DFK-Mining Profitability Tool
The purpose of this project is to show the profitability or loss of your heroes questing in the gas token value using the Dexscreener API. The method to determine this is simple. You need to subtract the gas you paid from questing from the value of your returned materials in the gas token. Before the Dexscreener API came along however this was a tedious and difficult task because you could not get the material prices in one place programatically to compare them with their gas token value. Once the Dexscreener API came out I built this project and added it to my DFK-Summoning Sheet website.  


## Quick Start
### DFK-Summoning Sheet
To get a summoning sheet sample simply take the inputs provided in summoning_sheet_sample.txt and put them in the form at [https://scientifik.pythonanywhere.com/heroform/.](https://scientifik.pythonanywhere.com/heroform/)

### DFK-Mining Profitability Tool
To get a sample material mining profit analysis take the inputs provided in mats_profitability_sample.txt and put them in the form at [https://scientifik.pythonanywhere.com/matsform/.](https://scientifik.pythonanywhere.com/matsform/)


## Usage
In order to use either of these projects comprehensively first get a feel for playing the game at [https://defikingdoms.com/.](https://defikingdoms.com) and then follow the tutorials at [https://scientifik.pythonanywhere.com/.](https://scientifik.pythonanywhere.com)

## Included Files
Files included in this project include but are not limited to.

- This README.md file
- A CHANGELOG.md file showing version control history and upgrades I plan on making.
- A templates folder holding Jinja templates for front end rendering.
- Module files which app.py rely on to get and create data for rendering.
- An app.py file which is responsible for the routing of GET and POST requests as well as rendering the front end content.

## On Production Server
- Change the relative path of the descreener_dfk_mats_prices.json file in dexscreener_api.py to the path of the wgsi.py file. This is the only variable which needs to be changed manually so I avoided making environment variables just to handle this.
