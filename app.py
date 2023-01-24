from flask import Flask, render_template
import requests
from summoning_stat_calculations import SummonStatistics

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start_sheet/')
def start_sheet():
    your_hero = 174708
    sd_1_candidate_list = (250575,)
    sd_2_candidate_list = tuple()
    cv_candidate_list = (113331, 62414, 53627, 38688)
    one_minus = lambda *x: 1 - sum(x)
    

    def return_hero_number_prefix(hero_num):
        prefix = '1' if hero_num in cv_candidate_list else '2'
        padding = '0'
        
        while len(prefix + padding + str(hero_num)) < 13:
            padding += '0'
        
        return int(prefix + padding + str(hero_num))
    

    final_list = (sd_1_candidate_list + tuple(map(return_hero_number_prefix,cv_candidate_list)) + tuple(map(return_hero_number_prefix, sd_2_candidate_list)))
    normalized_ids = (sd_1_candidate_list + cv_candidate_list + sd_2_candidate_list)
    character_stats = ('Strength', 'Agility', 'Intelligence', 'Wisdom', 'Luck', 'Vitality', 'Endurance', 'Dexterity')
    summon_odds_list = [SummonStatistics(your_hero, candidate).stats_genes_dictionary() for candidate in final_list]
    
    for i in range(len(summon_odds_list)):
        summon_odds_list[i].update({'hero_num': normalized_ids[i]})
        for stat in character_stats:
            summon_odds_list[i].update({'purple_stat_boost': {stat: summon_odds_list[i].get('stat_boost1').get(stat, 0) * summon_odds_list[i].get('stat_boost2').get(stat, 0)}})

    wanted_profession, hero_1_class = SummonStatistics(your_hero, final_list[0]).wanted_profession_and_hero_1_class()
    table_header = ('', 'profession', 'purple stats', 'blue stats', 'green stats', 'wanted classes','indifferent classes', 'other classes')
    header_span_list = (1,4,2,3,3,3,3,1)
    header_span_dict = {key:value for key,value in zip(table_header, header_span_list)}
    stat_keys = ('hero_num', 'profession', 'purple_stat_boost', 'stat_boost2', 'stat_boost1', 'main_class')
    character_class = ("Warrior", "Knight", "Thief", "Archer", "Priest", "Wizard", "Monk", "Pirate", "Berserker", "Seer", "Legionnaire", "Scholar", "Paladin", "DarkKnight", "Summoner", "Ninja", "Shapeshifter", "Bard", "Dragoon", "Sage", "SpellBow", "DreadKnight")
    wanted_stats_by_profession = {'Mining': ('Strength','Endurance'), 'Fishing': ('Agility', 'Luck'), 'Foraging': ('Dexterity', 'Intelligence'), 'Gardening': ('Wisdom', 'Vitality')}
    wanted_stat_1, wanted_stat_2 = wanted_stats_by_profession.get(wanted_profession)
    profession_order_by_wanted_profession = {'Mining': ('Mining', 'Foraging', 'Fishing', 'Gardening'), 'Foraging': ('Foraging', 'Gardening', 'Fishing', 'Mining'), 'Fishing': ('Fishing', 'Mining', 'Foraging', 'Gardening'), 'Gardening': ('Gardening', 'Foraging', 'Fishing', 'Mining')}
    desired_profession, second_choice, whiffed_profession, worst_profession = profession_order_by_wanted_profession.get(wanted_profession) 
    pre_class_stats = ('Normalized Id', desired_profession, second_choice, whiffed_profession, worst_profession, wanted_stat_1, wanted_stat_2, wanted_stat_1, wanted_stat_2, 'Other', wanted_stat_1, wanted_stat_2, 'Other') 
    table_subheader_dict = {'Warrior': ('Paladin', 'Warrior', 'Knight', 'DarkKnight', 'Archer', 'Thief', 'Other'), 'Knight': ('Paladin', 'Warrior', 'Knight', 'DarkKnight', 'Archer', 'Thief', 'Other'), 'Thief': ('DarkKnight', 'Thief', 'Archer', 'Paladin', 'Warrior', 'Knight', 'Other'), 'Archer': ('DarkKnight', 'Thief', 'Archer', 'Paladin', 'Warrior', 'Knight', 'Other'), 'Priest': ('Summoner', 'Priest', 'Wizard', 'Ninja', 'Monk', 'Pirate', 'Other'), 'Wizard': ('Summoner', 'Priest', 'Wizard', 'Ninja', 'Monk', 'Pirate', 'Other'), 'Monk': ('Ninja', 'Monk', 'Pirate', 'Summoner', 'Priest', 'Wizard', 'Other'), 'Pirate': ('Ninja', 'Monk', 'Pirate', 'Summoner', 'Priest', 'Wizard', 'Other'), 'Berserker': ('Shapeshifter', 'Berserker', 'Seer', 'Bard', 'Legionnaire', 'Scholar', 'Other'), 'Seer': ('Shapeshifter', 'Berserker', 'Seer', 'Bard', 'Legionnaire', 'Scholar','Other'), 'Legionnaire': ('Bard', 'Legionnaire', 'Scholar', 'Shapeshifter', 'Berserker', 'Seer', 'Other'), 'Scholar': ('Bard', 'Legionnaire', 'Scholar', 'Shapeshifter', 'Berserker', 'Seer', 'Other'), 'Paladin': ('Dragoon', 'Paladin', 'DarkKnight','Sage', 'Ninja', 'Summoner', 'Other'), 'DarkKnight': ('Dragoon', 'Paladin', 'DarkKnight', 'Sage', 'Ninja', 'Summoner', 'Other'), 'Summoner': ('Sage', 'Summoner', 'Ninja', 'SpellBow', 'Seer', 'Legionnaire', 'Other'), 'Ninja': ('Sage', 'Summoner', 'Ninja', 'SpellBow', 'Seer', 'Legionnaire', 'Other'), 'Shapeshifter': ('SpellBow', 'Shapeshifter', 'Bard', 'Sage', 'Summoner', 'Ninja', 'Other'), 'Bard': ('SpellBow', 'Shapeshifter', 'Bard', 'Sage', 'Summoner', 'Ninja', 'Other'), 'Dragoon': ('DreadKnight', 'Dragoon', 'Sage', 'SpellBow', 'Other'), 'Sage': ('DreadKnight', 'Dragoon', 'Sage', 'SpellBow', 'Other'), 'DreadKnight': ('DreadKnight', 'Dragoon', 'Sage', 'SpellBow', 'Other')} 
    hero_classes_list = table_subheader_dict.get(hero_1_class)
    table_subheader = pre_class_stats + table_subheader_dict.get(hero_1_class)
    table_row_dict_list = tuple({key:summon.get(key) for key in stat_keys} for summon in summon_odds_list) 
    pre_class_table_rows = tuple((row.get('hero_num'), row.get('profession').get(desired_profession), row.get('profession').get(second_choice, 0), row.get('profession').get(whiffed_profession, 0), row.get('profession').get(worst_profession, 0), row.get('purple_stat_boost').get(wanted_stat_1, 0), row.get('purple_stat_boost').get(wanted_stat_2, 0), row.get('stat_boost2').get(wanted_stat_1, 0), row.get('stat_boost2').get(wanted_stat_2, 0), one_minus(row.get('stat_boost2').get(wanted_stat_1, 0), row.get('stat_boost2').get(wanted_stat_2, 0)) , row.get('stat_boost1').get(wanted_stat_1, 0), row.get('stat_boost1').get(wanted_stat_2, 0), one_minus(row.get('stat_boost1').get(wanted_stat_1, 0), row.get('stat_boost1').get(wanted_stat_2, 0))) for row in table_row_dict_list)
    post_class_table_rows = tuple(tuple(1 - sum(tuple(row.get('main_class').get(hero_type, 0) for hero_type in hero_classes_list if hero_type != 'Other')) if hero_class == 'Other' else row.get('main_class').get(hero_class, 0) for hero_class in hero_classes_list) for row in table_row_dict_list)
    table_rows = (pre_class_list + post_class_list for pre_class_list, post_class_list in zip(pre_class_table_rows, post_class_table_rows))

    return render_template('start_sheet.html', table_rows = table_rows, table_header = table_header, header_span = header_span_dict, table_subheader = table_subheader)


app.route('/about/')
def about():
    return render_template('about.html')


app.run()
