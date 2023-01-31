'''
1) work on getting rarity stats
2) move onto front end
'''

from gene_class import HeroGenetics

class SummonStatistics:
    gene_type_list = ('dominant', 'recessive_1', 'recessive_2', 'recessive_3')
    full_class_list = ('Warrior', 'Knight', 'Archer', 'Thief', 'Pirate', 'Monk', 'Wizard', 'Priest', 'Seer', 'Beserker', 'Scholar', 'Legionaire', 'Paladin', 'DarkKnight', 'Ninja', 'Summoner', 'Shapeshifter', 'Bard', 'SpellBow', 'Dragoon', 'Sage', 'DreadKnight')
    #wanted_class_dictionary = self._wanted_class_dictionary() 
    

    def __init__(self, hero_1, hero_2):
        self.hero_1_stats_genes = HeroGenetics(hero_1).stats_gene_dictionary()
        self.hero_2_stats_genes = HeroGenetics(hero_2).stats_gene_dictionary()
        self.hero_1_visual_genes = HeroGenetics(hero_1).visual_gene_dictionary()
        self.hero_2_visual_genes = HeroGenetics(hero_2).visual_gene_dictionary()
        self._class_mutability_dictionary = {'main_class': self._is_mutatable('main_class'),'sub_class': self._is_mutatable('sub_class')}
        self._profession_to_pass = self.hero_1_stats_genes.get('profession').get('dominant')
        self._hero_1_class = self.hero_1_stats_genes.get('main_class').get('dominant')
        

    def _mutation_dictionary(self):
        mutatable_class_lists = [('Warrior','Knight'),('Archer','Thief'),('Pirate','Monk'),('Wizard','Priest'),('Seer','Beserker'),('Scholar','Legionaire'),('Paladin','DarkKnight'),('Ninja','Summoner'),('Shapeshifter','Bard'),('Dragoon','Sage')]
        final_list = mutatable_class_lists + [reversed(lst) for lst in mutatable_class_lists]
        return {key:value for key,value in final_list}


    def _is_mutatable(self, class_selector):
        hero_1_classes = self.hero_1_stats_genes.get(class_selector)
        hero_2_classes = self.hero_2_stats_genes.get(class_selector)

        mutation_check = lambda x,y: True if x == y else False
        mutation_dictionary = self._mutation_dictionary()

        return {key:mutation_check(mutation_dictionary.get(hero_1_classes.get(key)),hero_2_classes.get(key)) for key in SummonStatistics.gene_type_list}


    def _mutation_class_and_multiplier(self, tple):
        advanced_classes = ['Ninja', 'Summoner', 'Paladin', 'DarkKnight', 'Shapeshifter', 'Bard']
        elite_classes = ['Dragoon', 'Sage', 'SpellBow']
        exalted_classes = ['DreadKnight']
        keys_list = advanced_classes + elite_classes + exalted_classes
        summon_combinators = [('Monk', 'Pirate'), ('Priest', 'Wizard'), ('Warrior', 'Knight'), ('Thief', 'Archer'), ('Seer', 'Beserker'), ('Scholar', 'Legionaire'), ('Paladin', 'DarkKnight'), ('Ninja', 'Summoner'), ('Shapeshifter', 'Bard'), ('Dragoon', 'Sage')]
        reversed_combinators = [tuple(reversed(item)) for item in summon_combinators]
        mutation_class_dictionary = {key:value for key,value in zip(keys_list,zip(summon_combinators,reversed_combinators))}
        mutation_multiplier = None

        for key in keys_list:
            if tple in mutation_class_dictionary.get(key):
                mutation_multiplier = .125 if key in exalted_classes else .25 
                return key, mutation_multiplier
        
        return f'{tple} mutation combo not found!',0
    

    def _remaining_stats_steps(stats):
        def with_or_without_mutation(self,gene_type_selector,genetic_stat_set_key):
            hero_1_odds, hero_2_odds = stats(self, gene_type_selector, genetic_stat_set_key)
            mutability_dictionary = self._class_mutability_dictionary.get(genetic_stat_set_key, {key:False for key in tuple(hero_1_odds.keys())})
            hero_1_stats = self.hero_1_visual_genes.get(genetic_stat_set_key) if gene_type_selector == 'visual_genes' else self.hero_1_stats_genes.get(genetic_stat_set_key)
            hero_2_stats = self.hero_2_visual_genes.get(genetic_stat_set_key) if gene_type_selector == 'visual_genes' else self.hero_2_stats_genes.get(genetic_stat_set_key)
            hero_1_value_dictionary = {key:hero_1_odds.get(key,0) for key in SummonStatistics.gene_type_list}
            hero_2_value_dictionary = {key:hero_2_odds.get(key,0) for key in SummonStatistics.gene_type_list}
            child_stats_odds = {key:0 for key in list(hero_1_stats.values()) + list(hero_2_stats.values())}
            child_odds_final_step = lambda x: x * .5
            i = len(SummonStatistics.gene_type_list) -1

            while i >= 0:
                hero_1_mutation_index = i
                hero_2_mutation_index = i
                hero_1_stat_pass_odds = hero_1_value_dictionary.get(SummonStatistics.gene_type_list[hero_1_mutation_index])
                hero_2_stat_pass_odds = hero_2_value_dictionary.get(SummonStatistics.gene_type_list[hero_2_mutation_index])
                return_hero_1_and_hero_2_stat = lambda: (hero_1_stats.get(SummonStatistics.gene_type_list[hero_1_mutation_index]), hero_2_stats.get(SummonStatistics.gene_type_list[hero_2_mutation_index]))
                iteration_bypass_hero_1_and_hero_2_stat = lambda: (hero_1_stats.get(SummonStatistics.gene_type_list[hero_1_mutation_index - 1]), hero_2_stats.get(SummonStatistics.gene_type_list[hero_2_mutation_index - 1]))
            
                if mutability_dictionary.get(SummonStatistics.gene_type_list[i]) == True:
                    hero_1_stat, hero_2_stat = return_hero_1_and_hero_2_stat()
                    bypass_h1, bypass_h2 = iteration_bypass_hero_1_and_hero_2_stat()
                    
                    #handles the rare occurance of both hero_1 stat and hero_2 stat matching mutation stat on two or more consecutive levels at the same time
                    if hero_1_stat == bypass_h1 and hero_2_stat == bypass_h2:
                        i -= 1
                        continue

                    else:
                        while hero_1_stat_pass_odds == 0:
                            hero_1_mutation_index -= 1
                            hero_1_stat_pass_odds = hero_1_value_dictionary.get(SummonStatistics.gene_type_list[hero_1_mutation_index])

                        while hero_2_stat_pass_odds == 0:
                            hero_2_mutation_index -= 1
                            hero_2_stat_pass_odds = hero_2_value_dictionary.get(SummonStatistics.gene_type_list[hero_2_mutation_index])

                        child_mutation_class, child_mutation_multiplier = self._mutation_class_and_multiplier((hero_1_stat, hero_2_stat))
                        child_mutation_odds = hero_1_stat_pass_odds * hero_2_stat_pass_odds * child_mutation_multiplier
                        hero_1_stat_pass_odds -= child_mutation_odds
                        hero_2_stat_pass_odds -= child_mutation_odds
                        child_stats_odds[hero_1_stat] += child_odds_final_step(hero_1_stat_pass_odds)
                        child_stats_odds[hero_2_stat] += child_odds_final_step(hero_2_stat_pass_odds)
                        child_stats_odds_mutation_stat_check = True if child_stats_odds.get(child_mutation_class,False) == False else False

                        #if/else checks to see if the mutation stat is already in the child_mutation_odds dictionary and adds the key:value pair if not already present.
                        if child_stats_odds_mutation_stat_check:
                            child_stats_odds.update({child_mutation_class:child_mutation_odds})

                        else:
                            child_stats_odds[child_mutation_class] += child_mutation_odds

                else:
                    hero_1_stat, hero_2_stat = return_hero_1_and_hero_2_stat()
                    child_stats_odds[hero_1_stat] += child_odds_final_step(hero_1_stat_pass_odds)
                    child_stats_odds[hero_2_stat] += child_odds_final_step(hero_2_stat_pass_odds)

                i -= 1
            return child_stats_odds
        return with_or_without_mutation


    @_remaining_stats_steps
    def _initial_stats_step(self, gene_type_selector, genetic_stat_set_key):

        def _stats_compressor(stat_set):
            keys_list = stat_set.keys()
            stats_list = [.75, .1875, .046875, .015625]
            odds_dict = lambda x: {key:value for key,value in zip(x,stats_list)}
            return_dict = odds_dict(keys_list)
            stat_keys = tuple(keys_list)
            i = len(stat_keys)-1

            while i >= 1:
                if stat_set.get(stat_keys[i]) == stat_set.get(stat_keys[i-1]):
                    return_dict[stat_keys[i-1]] += return_dict[stat_keys[i]]
                    del return_dict[stat_keys[i]]

                i -= 1
            return return_dict

        hero_1_stat_set = self.hero_1_visual_genes.get(genetic_stat_set_key) if gene_type_selector == 'visual_genes' else self.hero_1_stats_genes.get(genetic_stat_set_key)
        hero_2_stat_set = self.hero_2_visual_genes.get(genetic_stat_set_key) if gene_type_selector == 'visual_genes' else self.hero_2_stats_genes.get(genetic_stat_set_key)
        hero_1_odds = _stats_compressor(hero_1_stat_set) 
        hero_2_odds = _stats_compressor(hero_2_stat_set) 
            
        
        return hero_1_odds, hero_2_odds


    def stats_genes_dictionary(self):
        return {key:self._initial_stats_step('stats_genes', key) for key in HeroGenetics.stat_keys}


    def visual_gene_dictionary(self):
        return {key:self._initial_stats_step('visual_genes', key) for key in HeroGenetics.visual_keys}
    

    def wanted_profession_and_hero_1_class(self):
        return self._profession_to_pass, self._hero_1_class




#summon = SummonStatistics(174708, 250575)
#child_stats_dict = summon.stats_genes_dictionary()
#child_stats_dict = summon.visual_gene_dictionary()
#child_stats_dict = summon.wanted_profession_and_hero_1_class()
#print(f'{child_stats_dict}')
