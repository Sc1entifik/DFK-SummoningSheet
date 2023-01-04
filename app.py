from flask import Flask, render_template
import requests
from summoning_stat_calculations import SummonStatistics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start_sheet/')
def start_sheet():
    summon = SummonStatistics(174708, 250575)
    stats_keys = ('element', 'stat_boost1', 'stat_boost2', 'profession', 'sub_class', 'main_class')
    character_stats = ('Strength','Agility','Intelligence','Wisdom','Luck','Vitality','Endurance','Dexterity')
    character_class = ("Warrior", "Knight", "Thief", "Archer", "Priest", "Wizard", "Monk", "Pirate", "Berserker", "Seer", "Legionnaire", "Scholar", "Paladin", "DarkKnight", "Summoner", "Ninja", "Shapeshifter", "Bard", "Dragoon", "Sage", "SpellBow", "DreadKnight")
    stats_keys_keys_tuple = (('Fire','Water','Wind','Lightning','Ice','Light','Dark'),character_stats,character_stats,('Mining', 'Fishing', 'Foraging', 'Gardening'), character_class, character_class)
    stats_keys_dictionary = {key:value for key,value in zip(stats_keys,stats_keys_keys_tuple)}
    child_stats_dict = summon.stats_genes_dictionary()
    return render_template('start_sheet.html', stats_keys = stats_keys, stats_keys_dictionary= stats_keys_dictionary, child_dict = child_stats_dict)


@app.route('/about/')
def about():
    return render_template('about.html')


app.run()
