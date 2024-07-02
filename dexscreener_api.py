import requests
import json
from datetime import datetime as dt

class DexscreenerStaticValues:
    DEXSCREENER_DATABASE_FILEPATH = "dexscreener_dfk_mats_prices.json"
    CHAIN_ID = "avalanchedfk"
    DATABASE_DATETIME_FORMAT = "%Y/%m/%d %H:%M"
    ITEM_QUERY_ENDPOINT = "https://api.dexscreener.com/latest/dex/search?q="
    MULTIPLE_ITEM_ENDPOINT = f"https://api.dexscreener.io/latest/dex/pairs/{CHAIN_ID}/"
    FISH_LIST = ("dfkbloater", "dfkironscale", "dfklanterneye", "dfkredgill", "dfksilverfin", "dfksailfish", "dfkfbloater", "dfkspckltl", "dfkthreel", "dfkkingpncr")
    PLANT_LIST= ("dfkrgwd", "dfkrckrt", "dfkrdlf", "dfkdrkwd", "dfkambrtfy", "dfkgldvn", "dfkswfthsl", "dfkfrostdrm", "dfkknaproot", "dfkdrkwd", "dfkshagcap", "dfksknshade", "dfkbluestem", "dfkspidrfrt", "dfkmilkweed")
    STONES_LIST = ("dfkshvas", "dfkmoksha", "dfklmghtcr", "dfklswftcr", "dfklfrticr", "dfklinscr", "dfklvgrcr", "dfklwitcr", "dfklfrtucr")
    TEARS_AND_EGGS_LIST = ("dfktears", "dfkblueegg", "dfkgregg", "dfkgreenegg", "dfkyelowegg", "dfkgoldegg")
    CURRENCIES = ("dfkgold", "klay")
    

class InitializeDexscreenerJsonDatabase(DexscreenerStaticValues):
    
    def _update_single_database_entry(self, query_item):
        dexscreener_object = requests.get(DexscreenerDatabaseManager.ITEM_QUERY_ENDPOINT + query_item).json().get("pairs") 
        
        for item in dexscreener_object:
            if item.get("chainId") == DexscreenerDatabaseManager.CHAIN_ID:

                return {"pair_address":item.get("pairAddress"), "price_native":item.get("priceNative"), "updated_at_last_update":True} 
    

    def initialize_dexscreener_dfk_mats_prices_json(self):
        full_item_list = DexscreenerDatabaseManager.FISH_LIST + DexscreenerDatabaseManager.PLANT_LIST + DexscreenerDatabaseManager.STONES_LIST + DexscreenerDatabaseManager.TEARS_AND_EGGS_LIST + DexscreenerDatabaseManager.CURRENCIES
        initial_database = map(self._update_single_database_entry, full_item_list) 

        with open(DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH, "w") as dexscreener_database:
            json.dump({key:value for key, value in zip(full_item_list, initial_database)} | {"last_updated": dt.now().strftime(DexscreenerDatabaseManager.DATABASE_DATETIME_FORMAT)}, dexscreener_database)
    

class DexscreenerDatabaseManager(DexscreenerStaticValues): 
    def __init__(self):
        self.dexscreener_dfk_mats_dictionary = self._load_dexscreener_dictionary()


    def _load_dexscreener_dictionary(self):
        with open(DexscreenerDatabaseManager.DEXSCREENER_DATABASE_FILEPATH) as dexscreener_database:
            dexscreenner_dictionary = json.load(dexscreener_database)
        
        return dexscreenner_dictionary

        
    def _return_updated_database(self):
        update_database_entries = lambda endpoint: {entry.get("baseToken").get("symbol").lower():entry for entry in requests.get(endpoint).json().get("pairs")}
        pair_address_dictionary  = lambda mats_list: {mat:self.dexscreener_dfk_mats_dictionary.get(mat).get("pair_address") for mat in mats_list }
        multiple_item_endpoint = lambda pair_address_dictionary: DexscreenerDatabaseManager.MULTIPLE_ITEM_ENDPOINT + ",".join(pair_address_dictionary.get(key) for key in pair_address_dictionary.keys())

        updated_database = update_database_entries(multiple_item_endpoint(pair_address_dictionary(DexscreenerDatabaseManager.FISH_LIST + DexscreenerDatabaseManager.PLANT_LIST))) | update_database_entries(multiple_item_endpoint(pair_address_dictionary(DexscreenerDatabaseManager.STONES_LIST + DexscreenerDatabaseManager.TEARS_AND_EGGS_LIST + DexscreenerDatabaseManager.CURRENCIES)))

        return updated_database


       
        
    
#initializer = InitializeDexscreenerJsonDatabase()
dexscreener = DexscreenerDatabaseManager()
#initializer.initialize_dexscreener_dfk_mats_prices_json()
prices_dict = dexscreener._return_updated_database()

for mat in prices_dict:
    print(f"{mat}: {prices_dict.get(mat).get("priceNative")}") 

