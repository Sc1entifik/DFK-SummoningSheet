# DFK-Summoning Sheet And DFK-Mining Profitability Tool
This project contains the DFK-Summoning Sheet and DFK-Mining Profitability Tool in one website at [https://scientifik.pythonanywhere.com/](https://scientifik.pythonanywhere.com/) since they go together like peanut butter and jelly. These are tools to be used with the [Defi Kingdoms web3 crypto game.](https://defikingdoms.com/) 
This is a Python Flask website.

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


## Contributing
These projects are highly opinionated and as a result I am not accepting PRs of any type. You are free to send any bug reports you have to [fullstackswe@drosenberry.dev](mailto:fullstackswe@drosenberry.dev) however. 


## Running Locally
You are free to clone the repo and play with the project locally. The following are instructions for that.

### Clone The Repo
Fork the repo at https://github.com/Sc1entifik/DFK-SummoningSheet.git then git clone your forked repo.

### Set Up A Venv 
In the root of the cloned fork run `python -m venv venv` to create a virtual environment

### Activate Your Venv And Install Requirements.txt
Now that you created a python virtual environment run `source venv/bin/activate` to activate your virtual environment.
Once your virtual environment is activated run `pip install -r requirements.txt`

### Create a .env file
There is a template environment variable file called environment_template.txt. Copy this file as .env by running `cp environment_template.txt .env` 

### Fill Out Your .env File
run `python generate_secret_key.py` this will print out a random secret key. Copy this key and then paste it in SECRET_KEY in your .env file.
Fill out ENVIRONMENT_TYPE=development.

### Run The Site
Make sure you are still in your virtual environment and then run `python app.py`. You should then be able to access the site locally from your browser with localhost:5000. If you want to use it from another computer on your network check out the address provided at the terminal acting as the local dev server. It should tell you the local socket address to use.
