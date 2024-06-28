import requests
import json

class DexScreenerPrices:
    PAIR_ADDRESS_FILEPATH = "pair_addresses.json"
    CHAIN_ID = "avalanchedfk"
    ITEM_QUERY_ENDPOINT = "https://api.dexscreener.com/latest/dex/search?q="
    MULTIPLE_ITEM_ENDPOINT = f"https://api.dexscreener.io/latest/dex/pairs/{CHAIN_ID}/"
    FISH_LIST = ("dfkbloater", "dfkironscale", "dfklanterneye", "dfkredgill", "dfksilverfin", "dfksailfish", "dfkfbloater", "dfkspckltl", "dfkthreel", "dfkkingpncr")
    PLANT_LIST= ("dfkrgwd", "dfkrckrt", "dfkrdlf", "dfkdrkwd", "dfkambrtfy", "dfkgldvn", "dfkswfthsl", "dfkfrostdrm", "dfkknaproot", "dfkdrkwd", "dfkshagcap", "dfksknshade", "dfkbluestem", "dfkspidrfrt", "dfkmilkweed")
    STONES_LIST = ("dfkshvas", "dfkmoksha", "dfklmghtcr", "dfklswftcr", "dfklfrticr", "dfklinscr", "dfklvgrcr", "dfklwitcr", "dfklfrtucr")
    TEARS_AND_EGGS_LIST = ("dfktears", "dfktears", "dfkblueegg", "dfkgregg", "dfkgreenegg", "dfkyelowegg", "dfkgoldegg")
    CURRENCIES = ("dfkgold", "klay")
    

    def _get_pair_address(self, query_item):
        dexscreener_object = requests.get(DexScreenerPrices.ITEM_QUERY_ENDPOINT + query_item).json().get("pairs")

        return dexscreener_object[0].get("pairAddress") if dexscreener_object else "0x4a17077F000FB66162BA6067Dc7f5f844F140DEe" #Ternary statement handles bug where dfkredgill is sometimes not found at dexscreener. 0x address is the 0x pair address for redgill.


    def write_pair_addresses_json(self):
        full_item_list = DexScreenerPrices.FISH_LIST + DexScreenerPrices.PLANT_LIST + DexScreenerPrices.STONES_LIST + DexScreenerPrices.TEARS_AND_EGGS_LIST + DexScreenerPrices.CURRENCIES
        pair_addresses = map(self._get_pair_address, full_item_list) 

        with open(DexScreenerPrices.PAIR_ADDRESS_FILEPATH, "w") as pairs:
            json.dump({key:value for key, value in zip(full_item_list, pair_addresses)}, pairs)
        
        
    def wjewel_discovery_price_dictionary(self):
        wjewel_discovery_prices = lambda mats_list, endpoint: {key:value.get("priceNative") for key, value in zip(mats_list, requests.get(endpoint).json().get("pairs"))}

        with open(DexScreenerPrices.PAIR_ADDRESS_FILEPATH) as fp:
            pair_addresses_dictionary = json.load(fp)


        fish_and_plant_addresses = {mat:pair_addresses_dictionary.get(mat) for mat in DexScreenerPrices.FISH_LIST + DexScreenerPrices.PLANT_LIST}
        fish_and_plants_endpoint = DexScreenerPrices.MULTIPLE_ITEM_ENDPOINT + ",".join(fish_and_plant_addresses.get(key) for key in fish_and_plant_addresses.keys())
        all_other_mats_addresses = {mat:pair_addresses_dictionary.get(mat) for mat in DexScreenerPrices.STONES_LIST + DexScreenerPrices.TEARS_AND_EGGS_LIST + DexScreenerPrices.CURRENCIES}
        all_other_mats_endpoint = DexScreenerPrices.MULTIPLE_ITEM_ENDPOINT + ",".join(all_other_mats_addresses.get(key) for key in all_other_mats_addresses.keys())
        fish_and_plant_prices = wjewel_discovery_prices(fish_and_plant_addresses, fish_and_plants_endpoint)
        all_other_mats_prices = wjewel_discovery_prices(all_other_mats_addresses, all_other_mats_endpoint)

        return fish_and_plant_prices | all_other_mats_prices

'''
dexscreener = DexScreenerPrices()
prices_dict = dexscreener.wjewel_discovery_price_dictionary()
for mat in DexScreenerPrices.FISH_LIST + DexScreenerPrices.PLANT_LIST + DexScreenerPrices.STONES_LIST + DexScreenerPrices.TEARS_AND_EGGS_LIST + DexScreenerPrices.CURRENCIES:
    print(f"{mat}: {prices_dict.get(mat)}")
    print()
'''
