# DFK-Summoning Sheet

The purpose of this project is to create a website that will provide you the summoning data for your hero and all the heros you could summon with that hero to get a side by side comparisson to find the best possible summon for that hero as opposed to only being able to see the data for one summon at a time. 

## DFK-Mining Profitability Tool
This project allows players to see how much they are profiting or losing by mining with their heroes. This could have been a stand alone webpage and project but it goes so well with the summoning sheet I decided to put everything together on one site.

## Included Files
Files included in this project include but are not limited to.

- This README.md file
- A CHANGELOG.md file showing version control history and upgrades I plan on making.
- A templates folder holding Jinja templates for front end rendering.
- Module files which app.py rely on to get and create data for rendering.
- An app.py file which is responsible for the routing of GET and POST requests as well as rendering the front end content.

## On Production Server
- Change the relative path of the descreener_dfk_mats_prices.json file in dexscreener_api.py to the path of the wgsi.py file. This is the only variable which needs to be changed manually so I avoided making environment variables just to handle this.
