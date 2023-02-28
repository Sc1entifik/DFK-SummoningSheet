from summoning_stat_calculations import SummonStatistics

def return_class_header_dictionary():
    class_list = SummonStatistics.full_class_list
    result_list = [(('Paladin', 'Warrior', 'Knight'), ('DarkKnight', 'Archer', 'Thief')), (('DarkKnight', 'Thief', 'Archer'), ('Paladin', 'Warrior', 'Knight')), (('Ninja', 'Monk', 'Pirate'), ('Summoner', 'Priest', 'Wizard')), (('Summoner', 'Priest', 'Wizard'), ('Ninja', 'Monk', 'Pirate')), (('Shapeshifter', 'Berserker', 'Seer'), ('Bard', 'Legionnaire', 'Scholar')), (('Bard', 'Legionnaire', 'Scholar'), ('Shapeshifter', 'Berserker', 'Seer')), (('Dragoon', 'Paladin', 'DarkKnight'), ('Sage', 'Ninja', 'Summoner')),  (('Sage', 'Summoner', 'Ninja'), ('SpellBow', 'Seer', 'Legionnaire')), (('SpellBow', 'Shapeshifter', 'Bard'), ('Sage', 'Summoner', 'Ninja')), (('SpellBow', None, None), ('Paladin', 'DarkKnight', None)), (('DreadKnight', 'Dragoon', 'Sage'), ('SpellBow', None, None)), (('DreadKnight', 'Dragoon', 'Sage'), ('SpellBow', None, None))]
    i = len(result_list) - 1
    
    while i >= 0:
        result_list.insert(i, result_list[i])
        i -= 1

    return {key:value for key, value in zip(class_list, result_list)}


class StatsController:
    wanted_classes_dictionary = return_class_header_dictionary()
    wanted_stats_dictionary = {'Mining': ('Strength', 'Endurance'), 'Fishing': ('Agility', 'Luck'), 'Foraging': ('Dexterity', 'Intelligence'), 'Gardening': ('Wisdom', 'Vitality')}
    profession_order_dictionary = {'Mining': ('Mining', 'Foraging', 'Fishing', 'Gardening'), 'Foraging': ('Foraging', 'Gardening', 'Fishing', 'Mining'), 'Gardening': ('Gardening', 'Foraging', 'Fishing', 'Mining'),'Fishing': ('Fishing','Mining','Foraging','Gardening')}
    other_stats_or_classes = ('Other',)
    summon_rarity = ('common', 'uncommon', 'rare', 'legendary', 'mythic')
    character_stats = ('Strength', 'Agility', 'Intelligence', 'Wisdom', 'Luck', 'Vitality', 'Endurance', 'Dexterity')
    
    def __init__(self, hero_input_form):
        self.hero_input_form = hero_input_form
        self.summon_odds_list, self.wanted_profession, self.your_hero_class = self._return_summon_statistics_data()
        self.profession_order = StatsController.profession_order_dictionary.get(self.wanted_profession)
        self.wanted_stats = StatsController.wanted_stats_dictionary.get(self.wanted_profession)
        self.wanted_classes = StatsController.wanted_classes_dictionary.get(self.your_hero_class)[0]
        self.indifferent_classes = StatsController.wanted_classes_dictionary.get(self.your_hero_class)[1]
        


    def _return_hero_number_with_realm_prefix(self, hero_num, your_hero = False):
        your_hero_prefix = '1' if self.hero_input_form.your_hero_realm.data == 'Crystalvale' else '2'
        candidate_hero_prefix = '1' if hero_num in self.hero_input_form.cv_candidate_list.data.split() else '2'
        prefix = your_hero_prefix if your_hero == True else candidate_hero_prefix
        padding = '0'

        while len(prefix + padding + str(hero_num)) < 13:
            padding += '0'

        return int(prefix + padding + str(hero_num))


    def _return_candidate_summon_cost_list(self):
        sd_candidate_costs = tuple((0 for i in range(len(self.hero_input_form.sd_candidate_list.data.split())))) if self.hero_input_form.sd_summon_cost.data == '' else tuple(map(float, self.hero_input_form.sd_summon_cost.data.split()))
        cv_candidate_costs = tuple((0 for i in range(len(self.hero_input_form.cv_candidate_list.data.split())))) if self.hero_input_form.cv_summon_cost.data == '' else tuple(map(float, self.hero_input_form.cv_summon_cost.data.split()))
        sd_2_candidate_costs = tuple((0 for i in range(len(self.hero_input_form.sd_2_candidate_list.data.split())))) if self.hero_input_form.sd_2_summon_cost.data == '' else tuple(map(float, self.hero_input_form.sd_2_summon_cost.data.split()))

        return sd_candidate_costs + cv_candidate_costs + sd_2_candidate_costs


    def _return_summon_statistics_data(self):
        candidate_normalized_id_list = (self.hero_input_form.sd_candidate_list.data.split() + self.hero_input_form.cv_candidate_list.data.split() + self.hero_input_form.sd_2_candidate_list.data.split())
        candidate_id_list = (tuple(self.hero_input_form.sd_candidate_list.data.split()) + tuple(map(self._return_hero_number_with_realm_prefix, self.hero_input_form.cv_candidate_list.data.split())) + tuple(map(self._return_hero_number_with_realm_prefix, self.hero_input_form.sd_2_candidate_list.data.split())))
        candidate_summon_costs_list = self._return_candidate_summon_cost_list()
        your_hero = self.hero_input_form.your_hero.data if self.hero_input_form.your_hero_realm.data == 'Serendale' else self._return_hero_number_with_realm_prefix(self.hero_input_form.your_hero.data, your_hero = True)
        your_hero_summon_cost = 0 if self.hero_input_form.your_hero_summon_cost.data == ''  else float(self.hero_input_form.your_hero_summon_cost.data)
        summon_statistics_list = [SummonStatistics(your_hero, candidate) for candidate in candidate_id_list]
        summon_odds_list = [stats_dict.stats_genes_dictionary() for stats_dict in summon_statistics_list]
        wanted_profession, hero_1_class = summon_statistics_list[0].wanted_profession_and_hero_1_class()

        for i in range(len(summon_statistics_list)):
            summon_odds_list[i].update({'hero_num': candidate_normalized_id_list[i]})
            summon_odds_list[i].update({'rarity_odds': summon_statistics_list[i].summon_rarity_odds()})
            summon_odds_list[i].update({'summon_cost': your_hero_summon_cost + candidate_summon_costs_list[i]})
            summon_odds_list[i].update({'purple_stat_boost':{}})
            
            for stat in StatsController.character_stats:
                summon_odds_list[i]['purple_stat_boost'].update({stat: summon_odds_list[i].get('stat_boost1').get(stat, 0) * summon_odds_list[i].get('stat_boost2').get(stat, 0)})

        return summon_odds_list, wanted_profession, hero_1_class



    def _return_table_header_span_and_table_subheader(self):
        id_and_cost = ('Normalized ID', 'Summon Cost')
        summon_rarity = tuple(rarity.capitalize() for rarity in StatsController.summon_rarity)
        table_subheader = id_and_cost + self.profession_order + self.wanted_stats * 2 + StatsController.other_stats_or_classes + self.wanted_stats + StatsController.other_stats_or_classes + self.wanted_classes + self.indifferent_classes + StatsController.other_stats_or_classes + summon_rarity 
        table_header_span = (len(id_and_cost), len(self.profession_order), len(self.wanted_stats), len(self.wanted_stats)+1, len(self.wanted_stats)+1, len(self.wanted_classes), len(self.indifferent_classes), len(StatsController.other_stats_or_classes), len(summon_rarity))

        return table_header_span, table_subheader


    def _return_table_rows(self):
        summon_odds_list_fetch = lambda x: [ tuple(row.get(item[0]).get(item[1], 0) if type(item) == tuple else row.get(item) for row in self.summon_odds_list) for item in x]
        one_minus = lambda x: [1 - sum(x)]
        key_subkey_tuple_map = lambda key, lst: map(lambda x: (key, x), lst)
        
        dict_keys = ('hero_num', 'summon_cost', 'profession', 'purple_stat_boost', 'stat_boost2', 'stat_boost1', 'main_class', 'rarity_odds')
        profession_1, profession_2, profession_3, profession_4 = key_subkey_tuple_map('profession', self.profession_order) 
        purple_stat_1, purple_stat_2 = key_subkey_tuple_map('purple_stat_boost', self.wanted_stats) 
        blue_stat_1, blue_stat_2 = key_subkey_tuple_map('stat_boost2', self.wanted_stats)
        green_stat_1, green_stat_2 = key_subkey_tuple_map('stat_boost1', self.wanted_stats)
        wanted_class_1, wanted_class_2, wanted_class_3 = key_subkey_tuple_map('main_class', self.wanted_classes)
        indifferent_class_1, indifferent_class_2, indifferent_class_3 = key_subkey_tuple_map('main_class', self.indifferent_classes)
        common, uncommon, rare, legendary, mythic = key_subkey_tuple_map('rarity_odds' ,StatsController.summon_rarity)
        row_content_list = ('hero_num', 'summon_cost', profession_1, profession_2, profession_3, profession_4, purple_stat_1, purple_stat_2, blue_stat_1, blue_stat_2, green_stat_1, green_stat_2, wanted_class_1, wanted_class_2, wanted_class_3, indifferent_class_1, indifferent_class_2, indifferent_class_3, common, uncommon, rare, legendary, mythic)
        table_rows = [[row.get(item[0]).get(item[1],0) if type(item) == tuple else row.get(item) for row in self.summon_odds_list] for item in row_content_list]

        #inserts blue_stat_other, green_stat_other, and other_classes into table_rows
        table_indexes = {key:row_content_list.index(key) for key in row_content_list}
        other_stats_or_classes = lambda *x: [1 - sum(items) for items in zip(*map(lambda index: table_rows[index], x))] 
        blue_stat_other = other_stats_or_classes(table_indexes.get(blue_stat_1), table_indexes.get(blue_stat_2))
        green_stat_other = other_stats_or_classes(table_indexes.get(green_stat_1), table_indexes.get(green_stat_2))
        other_classes = other_stats_or_classes(table_indexes.get(wanted_class_1), table_indexes.get(wanted_class_2), table_indexes.get(wanted_class_3), table_indexes.get(indifferent_class_1), table_indexes.get(indifferent_class_2), table_indexes.get(indifferent_class_3))
        table_rows.insert(table_indexes.get(common), other_classes)
        table_rows.insert(table_indexes.get(wanted_class_1), green_stat_other)
        table_rows.insert(table_indexes.get(green_stat_1), blue_stat_other)

        return zip(*table_rows)  

        
    def return_table_headers_and_rows(self):
        table_header = (f'{self.hero_input_form.your_hero.data}\n Summon Candidates and Summoning Cost', 'Profession', 'Purple Stat Odds', 'Blue Stat Odds', 'Green Stat Odds', 'Wanted Class Odds', 'Indifferent Class Odds', 'Other Class Odds', 'Summoning Rarity Odds')
        table_header_span, table_subheader = self._return_table_header_span_and_table_subheader()
        header_span_dict = {key:value for key, value in zip(table_header, table_header_span)}
        table_rows = self._return_table_rows() 

        return(table_header, header_span_dict, table_subheader, table_rows)
             
