from summoning_stat_calculations import SummonStatistics

def class_header_dictionary():
    class_list = SummonStatistics.full_class_list
    result_list = [(('Paladin', 'Warrior', 'Knight'), ('DarkKnight', 'Archer', 'Thief')), (('DarkKnight', 'Thief', 'Archer'), ('Paladin', 'Warrior', 'Knight')), (('Ninja', 'Monk', 'Pirate'), ('Summoner', 'Priest', 'Wizard')), (('Summoner', 'Priest', 'Wizard'), ('Ninja', 'Monk', 'Pirate')), (('Shapeshifter', 'Berserker', 'Seer'), ('Bard', 'Legionnaire', 'Scholar')), (('Bard', 'Legionnaire', 'Scholar'), ('Shapeshifter', 'Berserker', 'Seer')), (('Dragoon', 'Paladin', 'DarkKnight'), ('Sage', 'Ninja', 'Summoner')),  (('Sage', 'Summoner', 'Ninja'), ('SpellBow', 'Seer', 'Legionnaire')), (('SpellBow', 'Shapeshifter', 'Bard'), ('Sage', 'Summoner', 'Ninja')), (('SpellBow', None, None), ('Paladin', 'DarkKnight', None)), (('DreadKnight', 'Dragoon', 'Sage'), ('SpellBow', None, None)), (('DreadKnight', 'Dragoon', 'Sage'), ('SpellBow', None, None))]
    i = len(result_list) - 1
    
    while i >= 0:
        result_list.insert(i, result_list[i])
        i -= 1

    return {key:value for key, value in zip(class_list, result_list)}


class StatsController:
    wanted_classes_dictionary = class_header_dictionary()
    wanted_stats_dictionary = {'Mining': ('Strength', 'Endurance'), 'Fishing': ('Agility', 'Luck'), 'Foraging': ('Dexterity', 'Intelligence'), 'Gardening': ('Wisdom', 'Vitality')}
    profession_order_dictionary = {'Mining': ('Mining', 'Foraging', 'Fishing', 'Gardening'), 'Foraging': ('Foraging', 'Gardening', 'Fishing', 'Mining'), 'Gardening': ('Gardening', 'Foraging', 'Fishing', 'Mining'),'Fishing': ('Fishing','Mining','Foraging','Gardening')}
    other_stats_or_classes = ('Other',)
    summon_rarity = ('common', 'uncommon', 'rare', 'legendary', 'mythic')
    character_stats = ('Strength', 'Agility', 'Intelligence', 'Wisdom', 'Luck', 'Vitality', 'Endurance', 'Dexterity')
    
    def __init__(self, hero_input_form):
        self.hero_input_form = hero_input_form
        self.summon_odds_list, self.wanted_profession, self.your_hero_class = self._summon_statistics_data()
        self.profession_order = StatsController.profession_order_dictionary.get(self.wanted_profession)
        self.wanted_stats = StatsController.wanted_stats_dictionary.get(self.wanted_profession)
        self.wanted_classes = StatsController.wanted_classes_dictionary.get(self.your_hero_class)[0]
        self.opposing_mutation_classes = StatsController.wanted_classes_dictionary.get(self.your_hero_class)[1]
        

    def _hero_number_with_realm_prefix(self, hero_num, your_hero = False):
        your_hero_prefix = '1' if self.hero_input_form.your_hero_realm.data == 'Crystalvale' else '2'
        candidate_hero_prefix = '1' if hero_num in (hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.cv_candidate_list.data.split()) else '2'
        prefix = your_hero_prefix if your_hero == True else candidate_hero_prefix
        padding = '0'
        hero_number_with_realm_prefix_length = 13

        while len(prefix + padding + str(hero_num)) < hero_number_with_realm_prefix_length:
            padding += '0'


        return int(prefix + padding + str(hero_num))


    def _candidate_summon_cost_list(self):
        sd_candidate_costs = (float(hero_and_cost.split(",", 1)[1]) if len(hero_and_cost.split(",", 1)) == 2 else 0 for hero_and_cost in self.hero_input_form.sd_candidate_list.data.split())
        cv_candidate_costs = (float(hero_and_cost.split(",", 1)[1]) if len(hero_and_cost.split(",", 1)) == 2 else 0 for hero_and_cost in self.hero_input_form.cv_candidate_list.data.split())
        sd_2_candidate_costs = (float(hero_and_cost.split(",", 1)[1]) if len(hero_and_cost.split(",", 1)) == 2 else 0 for hero_and_cost in self.hero_input_form.sd_2_candidate_list.data.split())

        return tuple(sd_candidate_costs) + tuple(cv_candidate_costs) + tuple(sd_2_candidate_costs)


    def _summon_statistics_data(self):
        candidate_normalized_id_list = ([hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.sd_candidate_list.data.split()] + [hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.cv_candidate_list.data.split()] + [hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.sd_2_candidate_list.data.split()])
        candidate_id_list = (tuple(hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.sd_candidate_list.data.split()) + tuple(map(self._hero_number_with_realm_prefix, (hero_and_cost.split("," ,1)[0] for hero_and_cost in self.hero_input_form.cv_candidate_list.data.split()))) + tuple(map(self._hero_number_with_realm_prefix, (hero_and_cost.split(",", 1)[0] for hero_and_cost in self.hero_input_form.sd_2_candidate_list.data.split()))))
        candidate_summon_costs_list = self._candidate_summon_cost_list()
        your_hero = self.hero_input_form.your_hero.data.split(",", 1)[0] if self.hero_input_form.your_hero_realm.data == 'Serendale' else self._hero_number_with_realm_prefix(self.hero_input_form.your_hero.data.split(",", 1)[0], your_hero = True)
        your_hero_summon_cost = float(self.hero_input_form.your_hero.data.split(",", 1)[1]) if len(self.hero_input_form.your_hero.data.split(",", 1)) == 2 else 0 
        summon_statistics_list = [SummonStatistics(your_hero, candidate) for candidate in candidate_id_list]
        summon_odds_list = [stats_dict.summon_stats_genetics_dictionary() for stats_dict in summon_statistics_list]
        wanted_profession, hero_1_class = summon_statistics_list[0].wanted_profession_and_hero_1_class()

        for i in range(len(summon_statistics_list)):
            summon_odds_list[i].update({'hero_num': candidate_normalized_id_list[i]})
            summon_odds_list[i].update({'rarity_odds': summon_statistics_list[i].summon_rarity_odds()})
            summon_odds_list[i].update({'summon_cost': your_hero_summon_cost + candidate_summon_costs_list[i]})
            summon_odds_list[i].update({'purple_stat_boost':{}})
            
            for stat in StatsController.character_stats:
                summon_odds_list[i]['purple_stat_boost'].update({stat: summon_odds_list[i].get('stat_boost1').get(stat, 0) * summon_odds_list[i].get('stat_boost2').get(stat, 0)})

        return summon_odds_list, wanted_profession, hero_1_class


    def _subheader_dictionary(self):
        return {
            "Gardening": "Gard",
            "Foraging": "Forg",
            "Fishing": "Fish",
            "Mining": "Mine",
            "Strength": "STR",
            "Dexterity": "DEX",
            "Agility": "AGI",
            "Vitality": "VIT",
            "Endurance": "END",
            "Intelligence": "INT",
            "Wisdom": "WIS",
            "Luck": "LCK"
        }
    

    def _optimized_controller(optimized_summon_odds_list):

        wrapper = lambda self: {"summon_odds_list": optimized_summon_odds_list(self), "your_hero_num": self.hero_input_form.your_hero.data.split(",")[0], "your_hero_cost": self.hero_input_form.your_hero.data.split(",")[1] if len(self.hero_input_form.your_hero.data.split(",")) > 1 else 0.0, "subheader_dictionary": self._subheader_dictionary(), "profession_order": self.profession_order, "wanted_stats": self.wanted_stats, "wanted_classes": self.wanted_classes, "opposing_mutation_classes": self.opposing_mutation_classes}

        return wrapper



    @_optimized_controller
    def optimized_summon_odds_list(self):
        wanted_stats = ("hero_num", "summon_cost", "profession", "purple_stat_boost", "stat_boost2", "stat_boost1", "main_class", "rarity_odds")
        optimized_key_names = ("hero_num", "summon_cost", "profession", "purple_stat_boost", "blue_stat_boost", "green_stat_boost", "class_odds", "rarity_odds")
        sub_dict_list = ("profession","purple_stat_boost", "blue_stat_boost", "green_stat_boost", "class_odds", "rarity_odds")
        optimized_summon_odds_list = [{optimized_key_names[i]: candidate[wanted_stats[i]] for i in range(len(optimized_key_names))} for candidate in self.summon_odds_list]
        
        for parent_dict in optimized_summon_odds_list:
            for sub_dict in sub_dict_list:
                for key, value in parent_dict.get(sub_dict).items():
                    if value:
                        parent_dict.get(sub_dict)[key] = round(value, 3)
            
            wanted_class_and_opposing_mutation_class_odds = 0

            for key in self.wanted_classes + self.opposing_mutation_classes:
                wanted_class_and_opposing_mutation_class_odds += parent_dict.get("class_odds").get(key, 0)

            lemon_odds = abs(1 - wanted_class_and_opposing_mutation_class_odds)
            parent_dict.get("class_odds").update({"lemon": round(lemon_odds, 3)})

        return optimized_summon_odds_list


class MatsController:
    CURRENCIES = ("crystal", "jewel", "gold")
    TEARS_AND_RUNES = ("tears", "shvas_rune", "moksha_rune")
    EGGS = ("blue_egg", "grey_egg", "green_egg", "yellow_egg")
    CRYSTALS = ("might_crystal", "swiftness_crystal", "fortitude_crystal", "insight_crystal", "finesse_crystal", "vigor_crystal", "wit_crystal", "fortune_crystal")
    FISH = ("bloater","ironscale","lantern_eye","redgill","silverfin","sailfish","shimmerskin","frost_bloater","speckle_tail","three_eyed_eel","king_pincer")
    PLANTS = ("ragweed","rockroot","redleaf","darkweed","ambertaffy","goldvein","swift_thistle","frost_drum","knaproot","shaggy_cap","skunkshade","bluestem","spiderfruit","milkweed")

    def __init__(self, form, mats_prices_dict):
        self.form = form
        self.transaction_currency = "jewel" if self.form.kingdom.data == "Crystalvale" else "klay"
        self.transaction_currency_image_source = f"../static/images/{self.transaction_currency}.png"
        self._mats_prices_dict = mats_prices_dict
        self.price_dictionary = self._price_key_conversion_dictionary()
        self.total_mats_profit = self._total_profits() 
        self.total_profit = round(self.total_mats_profit.get("materials_total") - self.form.transaction_cost.data, 5)


    # Converts the _mats_prices_dict to use the same keys as self.form.mats_keys
    def _price_key_conversion_dictionary(self):
        jewel_price = lambda x: round(float(self._mats_prices_dict.get(x).get("price_native")), 5)
        klay_price = lambda x: round(jewel_price(x) / round(float(self._mats_prices_dict.get("klay").get("price_native")), 5), 5)
        price_key_conversion_dictionary = {key: jewel_price(value) if self.transaction_currency == "jewel" else klay_price(value) for key, value in zip(self.form.mats_keys, self._mats_prices_dict.keys())} 
        price_key_conversion_dictionary.update({"jewel": 1 if self.transaction_currency == "jewel" else self._mats_prices_dict.get("klay").get("price_native")})

        return price_key_conversion_dictionary 

    
    def _total_profits(self):
        unwanted_keys = ("gold_egg", "klay")
        total_profit_dictionary = {key: round(float(self.price_dictionary.get(key)) * eval(f"self.form.{key}.data"), 5) for key in self.form.mats_keys if key not in unwanted_keys}
        total_profit_dictionary.update({"jewel": float(self.price_dictionary.get("jewel")) * self.form.jewel.data})
        total_profit_dictionary.update({"materials_total": round(sum(total_profit_dictionary.values()), 5)})

        return total_profit_dictionary 

    
    def display_dict_map(self, item_list):

        def display_dict(item):
            image_source = f"../static/images/{item}.png"
            item_quantity = eval(f"self.form.{item}.data")
            item_price = self.price_dictionary.get(item)
            item_profit = self.total_mats_profit.get(item)

            return {"image_source": image_source, "item_quantity": item_quantity, "item_price": item_price, "item_profit": item_profit}
        
        return map(display_dict, item_list)
