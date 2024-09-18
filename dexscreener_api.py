import requests
import json
from datetime import datetime, timedelta

class DexscreenerStaticValues:
    DEXSCREENER_DATABASE_FILEPATH = "dexscreener_dfk_mats_prices.json"
    CHAIN_ID = "avalanchedfk"
    DATABASE_DATETIME_FORMAT = "%Y/%m/%d %H:%M"
    ITEM_QUERY_ENDPOINT = "https://api.dexscreener.com/latest/dex/search?q="
    MULTIPLE_ITEM_ENDPOINT = f"https://api.dexscreener.io/latest/dex/pairs/{CHAIN_ID}/"
    FISH_LIST = ("dfkbloater", "dfkironscale", "dfklanterneye", "dfkredgill", "dfksilverfin", "dfkshimmerskin", "dfksailfish", "dfkfbloater", "dfkspckltl", "dfkthreel", "dfkkingpncr")
    PLANT_LIST= ("dfkrgwd", "dfkrckrt", "dfkrdlf", "dfkdrkwd", "dfkambrtfy", "dfkgldvn", "dfkswfthsl", "dfkfrostdrm", "dfkknaproot", "dfkshagcap", "dfksknshade", "dfkbluestem", "dfkspidrfrt", "dfkmilkweed")
    CRYSTAL_LIST = ("dfkshvas", "dfkmoksha", "dfklmghtcr", "dfklswftcr", "dfklfrticr", "dfklinscr","dfklfincr" ,"dfklvgrcr", "dfklwitcr", "dfklfrtucr")
    TEARS_AND_EGGS_LIST = ("dfktears", "dfkblueegg", "dfkgregg", "dfkgreenegg", "dfkyelowegg", "dfkgoldegg")
    CURRENCIES = ("dfkgold", "klay", "crystal")
    

class InitializeDexscreenerJsonDatabase(DexscreenerStaticValues):
    
    def _update_single_database_entry(self, query_item):
        dexscreener_object = requests.get(DexscreenerDatabaseManager.ITEM_QUERY_ENDPOINT + query_item).json().get("pairs") 
        
        for item in dexscreener_object:
            if item.get("chainId") == DexscreenerDatabaseManager.CHAIN_ID:

                return {"pair_address":item.get("pairAddress"), "price_native":item.get("priceNative"), "updated_at_last_update":True} 
    

    def initialize_dexscreener_dfk_mats_prices_json(self):
        full_item_list = DexscreenerDatabaseManager.FISH_LIST + DexscreenerDatabaseManager.PLANT_LIST + DexscreenerDatabaseManager.CRYSTAL_LIST + DexscreenerDatabaseManager.TEARS_AND_EGGS_LIST + DexscreenerDatabaseManager.CURRENCIES
        initial_database = map(self._update_single_database_entry, full_item_list) 

        with open(DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH, "w") as dexscreener_database:
            json.dump({key:value for key, value in zip(full_item_list, initial_database)} | {"last_updated": datetime.now().strftime(DexscreenerDatabaseManager.DATABASE_DATETIME_FORMAT)}, dexscreener_database)

        print(f"New materials database initialized at {InitializeDexscreenerJsonDatabase.DEXSCREENER_DATABASE_FILEPATH}")
    

class DexscreenerDatabaseManager(DexscreenerStaticValues): 

    def __init__(self):
        self.dexscreener_dfk_mats_dictionary = self._load_dexscreener_dictionary()


    def _load_dexscreener_dictionary(self):
        with open(DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH) as dexscreener_database:
            dexscreenner_dictionary = json.load(dexscreener_database)
            
        
        return dexscreenner_dictionary

        
    def _return_updated_database_dictionary(self):
        
        def updated_database_dictionary(multiple_item_endpoint):
            return lambda mats_list: {entry.get("baseToken").get("symbol").lower(): entry.get("priceNative") for entry in requests.get(multiple_item_endpoint(mats_list)).json().get("pairs")}

        @updated_database_dictionary
        def multiple_item_endpoint(mats_list):
            return DexscreenerDatabaseManager.MULTIPLE_ITEM_ENDPOINT + ",".join(self.dexscreener_dfk_mats_dictionary.get(mat).get("pair_address") for mat in mats_list)

        #There is a rate limit of thirty items per call on the mulitple item endpoint api. This is why it is necessary to break this up into two calls and then unite the dictionary with this union. 
        return multiple_item_endpoint(DexscreenerDatabaseManager.FISH_LIST + DexscreenerDatabaseManager.PLANT_LIST) | multiple_item_endpoint(DexscreenerDatabaseManager.CRYSTAL_LIST + DexscreenerDatabaseManager.TEARS_AND_EGGS_LIST + DexscreenerDatabaseManager.CURRENCIES) 


    def update_database_prices(self):
        updated_prices = self._return_updated_database_dictionary()
        mats_not_updated = (mat for mat in self.dexscreener_dfk_mats_dictionary.keys() if not updated_prices.get(mat))
        
        for mat in mats_not_updated:
            if mat != "last_updated": # "last_updated" key provides the datetime of the last time the database was updated. The rest of the keys return a mat.
                self.dexscreener_dfk_mats_dictionary.get(mat)["updated_at_last_update"] = False

        for mat in updated_prices.keys():
            self.dexscreener_dfk_mats_dictionary.get(mat)["price_native"] = updated_prices.get(mat)
            self.dexscreener_dfk_mats_dictionary.get(mat)["updated_at_last_update"] = True

        self.dexscreener_dfk_mats_dictionary["last_updated"] = datetime.now().strftime(self.DATABASE_DATETIME_FORMAT)


        with open(DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH, "w") as dexscreener_database:
            json.dump(self.dexscreener_dfk_mats_dictionary, dexscreener_database)

        print(f"Relational json database has been updated at {DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH}")


    def is_update_time(self):
        time_difference = datetime.now() - datetime.strptime(self.dexscreener_dfk_mats_dictionary.get("last_updated"), self.DATABASE_DATETIME_FORMAT)

        return time_difference >= timedelta(hours=6)
        


    
#initializer = InitializeDexscreenerJsonDatabase()
#dexscreener = DexscreenerDatabaseManager()
#initializer.initialize_dexscreener_dfk_mats_prices_json()
#dexscreener.update_database_prices()

'''
for mat, price in dexscreener.dexscreener_dfk_mats_dictionary.items():
    print(f"{mat}: {price}") 
'''
