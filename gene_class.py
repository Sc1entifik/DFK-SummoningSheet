import requests

class HeroGenetics():
    api_url = 'https://defi-kingdoms-community-api-gateway-co06z8vi.uc.gateway.dev/graphql'
    stat_keys = ('stats_unknown2','element','stats_unknown1','stat_boost2','stat_boost1','active2','active1','passive2','passive1','profession','sub_class','main_class')
    visual_keys = ('visual_unknown2','back_appendage_color','appendage_color','skin_color','eye_color','visual_unknown1','hair_color','hair_style','back_ground','back_appendage','head_appendage','gender')

    
    def __init__(self,hero_id):
        self.hero_id = hero_id
        self.hero_stat_gene_sequence = int(self._api_call())
        self.hero_visual_gene_sequence = int(self._api_call('visualGenes'))
        self._hero_rarity = int(self._api_call('rarity'))


    #can call the api for any stat that is callable from the dfk-api if you wish to add more instance variables in the __init__ function for your project 
    def _api_call(self,var_name='statGenes'):
        query = '''{{
        heroes(where: {{id:"{hero_id}"}}){{
        normalizedId
        {var_name}
         }}
        }}'''.format(hero_id=self.hero_id,var_name=var_name)
        result = requests.post(HeroGenetics.api_url, json={'query':query})
        gene_query_results = result.json()['data']['heroes']

        return gene_query_results[0].get(var_name)
        

    def _gene_sequence_decode(self,gene_selector):
        gene_sequence = self.hero_visual_gene_sequence if gene_selector == 'visual_genes' else self.hero_stat_gene_sequence
        r_num_key = lambda x: x%32
        decode_sequences = [gene_sequence]
        answer = gene_sequence
    
        for i in range(47):
            answer = answer//32
            decode_sequences.append(answer)

        r_num_lists = []
        append_list = []

        for i in map(r_num_key,decode_sequences):
            append_list.append(i)
            if len(append_list) == 4:
                r_num_lists.append(append_list)
                append_list = []
       
        return r_num_lists


    def _decoder_key_ring(self,dict_type):
        unused = {key:value for key,value in zip(range(30),["Information currently unused by game" for i in range(30)])}
        #stat gene decodings
        hero_class = {0: "Warrior", 1: "Knight", 2: "Thief", 3: "Archer", 4: "Priest", 5: "Wizard", 6: "Monk", 7: "Pirate", 8: "Berserker", 9: "Seer", 10: "Legionnaire", 11: "Scholar", 16: "Paladin", 17: "DarkKnight", 18: "Summoner", 19: "Ninja", 20: "Shapeshifter", 21: "Bard", 24: "Dragoon", 25: "Sage", 26: "SpellBow", 28: "DreadKnight"}
        profession = {0: "Mining", 2: "Gardening", 4: "Fishing", 6: "Foraging"}
        stats = {0: "Strength", 2: "Agility", 4: "Intelligence", 6: "Wisdom", 8: "Luck", 10: "Vitality", 12: "Endurance", 14: "Dexterity"}
        active_passive = {0: "Basic1", 1: "Basic2", 2: "Basic3", 3: "Basic4", 4: "Basic5", 5: "Basic6", 6: "Basic7", 7: "Basic8", 16: "Advanced1", 17: "Advanced2", 18: "Advanced3", 19: "Advanced4", 20: "Advanced5", 21: "Advanced6", 22: "Advanced7", 23: "Advanced8", 24: "Elite1", 25: "Elite2", 26: "Elite3", 27:"Elite4", 28: "Transcendant1", 29:"Transcendant2"}
        element = {0: "Fire", 2: "Water", 4: "Earth", 6: "Wind", 8: "Lightning", 10: "Ice", 12: "Light", 14: "Dark"}

        #visual gene decodings
        visual_unknown = {key:value for key,value in zip(range(30),['Information currently unused'for i in range(30)])}
        appendage_color = {0: "#c5bfa7", 1: "#a88b47", 2: "#58381e", 3: "#566f7d", 4: "#2a386d", 5: "#3f2e40", 6: "#830e18", 7: "#6f3a3c", 8: "#cddef0", 9: "#df7126", 10: "#835138", 11: "#86a637", 16: "#6b173c", 17: "#a0304d", 18: "#78547c", 19: "#352a51", 20: "#147256", 21: "#cf7794", 24: "#c29d35", 25: "#211f1f", 26: "#77b5cf", 28: "#d7d7d7"}
        skin_color = {0: "#c58135", 2: "#f1ca9e", 4: "#985e1c", 6: "#57340c", 8: "#e6a861", 10: "#7b4a11", 12: "#e5ac91", 14: "#aa5c38"}
        eye_color = {0: "#203997", 2: "#896693", 4: "#bb3f55", 6: "#0d7634", 8: "#8d7136", 10: "#613d8a", 12: "#2494a2", 14: "#a41e12"}
        hair_color = {0: "#ab9159", 1: "#af3853", 2: "#578761", 3: "#068483", 4: "#48321e", 5: "#66489e", 6: "#ca93a7", 7: "#62a7e6", 8: "#c34b1e", 9: "#326988", 10: "#513f4f", 11: "#d48b41", 16: "#d7bc65", 17: "#9b68ab",  18: "#8d6b3a", 19: "#566377", 20: "#275435", 21: "#77b23c", 24: "#880016", 25: "#353132", 26: "#dbfbf5", 28: "#8f9bb3"}
        hair_style = {"male": {0: "Battle Hawk", 1: "Wolf Mane", 2: "Enchanter", 3: "Wild Growth", 4: "Pixel", 5: "Sunrise", 6: "Bouffant", 7: "Agleam Spike", 8: "Wayfinder", 9: "Faded Topknot", 10: "Side Shave", 11: "Ronin", 16: "Gruff",  17: "Rogue Locs",  18: "Stone Cold", 19: "Zinra's Tail", 20: "Hedgehog", 21: "Delinquent", 24: "Skegg", 25: "Shinobi", 26: "Sanjo", 28: "Perfect Form"},
  "female": {0: "Windswept", 1: "Fauna", 2: "Enchantress", 3: "Pineapple Top", 4: "Pixie", 5: "Darkweave Plait", 6: "Dejanira", 7: "Courtly Updo", 8: "Centaur Tail", 9: "Lamia", 10: "Casual Ponytail", 11: "Wild Ponytail", 16: "Vogue Locs", 17: "Twin Vine Loops", 18: "Sweeping Willow", 19: "Odango", 20: "Goddess Locks", 21: "Lioness", 24: "Ethereal Waterfall", 25: "Kunoichi", 26: "???", 28: "Lunar Light Odango"}
}
        back_ground = {0: "Desert", 2: "Forest", 4: "Plains", 6: "Island", 8: "Swamp", 10: "Mountains", 12: "City", 14: "Arctic"}
        gender = {1: "Male", 3: "Female"}

        stats_list = [unused,element,unused,stats,stats,active_passive,active_passive,active_passive,active_passive,profession,hero_class,hero_class]
        visual_list = [unused,appendage_color,appendage_color,skin_color,eye_color,unused,hair_color,hair_style,back_ground,appendage_color,appendage_color,gender]
        return visual_list if dict_type == 'visual_genes' else stats_list


    def _decoded_gene_dictionary(self,dict_type):

        decoded_dictionary = self.visual_gene_encoded_dictionary() if dict_type == 'visual_genes' else self.stats_gene_encoded_dictionary()
        key_ring_keys = HeroGenetics.visual_keys if dict_type == 'visual_genes' else HeroGenetics.stat_keys
        decoder_key_ring = {key:value for key,value in zip(key_ring_keys,self._decoder_key_ring(dict_type))}

        for key in key_ring_keys:
            decode_list = decoded_dictionary.get(key)
            decoding_key = decoder_key_ring.get(key)
            decoded_dictionary[key] = {'dominant':decoding_key.get(decode_list[0]),'recessive_1':decoding_key.get(decode_list[1]),'recessive_2':decoding_key.get(decode_list[2]),'recessive_3':decoding_key.get(decode_list[3])}

        return decoded_dictionary


    def stats_gene_encoded_dictionary(self):
        return {key:value for key,value in zip(HeroGenetics.stat_keys,self._gene_sequence_decode('stat_genes'))}


    def visual_gene_encoded_dictionary(self):
        return {key:value for key,value in zip(HeroGenetics.visual_keys,self._gene_sequence_decode('visual_genes'))}


    def stats_gene_dictionary(self):
        return self._decoded_gene_dictionary('stat_genes') 


    def visual_gene_dictionary(self):
        return self._decoded_gene_dictionary('visual_genes')


    def hero_rarity(self):
        return self._hero_rarity
'''
your_hero = HeroGenetics(2000000014834)
rented_hero = HeroGenetics(1000000149421)
print(your_hero.stats_gene_dictionary())
print(rented_hero.stats_gene_dictionary())
'''
