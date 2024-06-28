import pytest
import json
from pathlib import Path

from dexscreener_api import DexScreenerPrices 

@pytest.fixture
def dexscreener_object():
    return DexScreenerPrices()

@pytest.fixture
def full_mats_list():
    return DexScreenerPrices.FISH_LIST + DexScreenerPrices.PLANT_LIST + DexScreenerPrices.STONES_LIST + DexScreenerPrices.TEARS_AND_EGGS_LIST + DexScreenerPrices.CURRENCIES


def test_write_pair_addresses_json(dexscreener_object):
    pair_address_filepath = Path(DexScreenerPrices.PAIR_ADDRESS_FILEPATH)
    
    if pair_address_filepath.is_file():
        pair_address_filepath.unlink()

    dexscreener_object.write_pair_addresses_json()

    assert pair_address_filepath.is_file()


def test_json_pair_addresses(full_mats_list):
    with open(DexScreenerPrices.PAIR_ADDRESS_FILEPATH) as pair_addresses:
        pair_address_dictionary = json.load(pair_addresses)


    for mat in full_mats_list:
        assert pair_address_dictionary.get(mat)[:2] == "0x"


def test_wjewel_discovery_price_dictionary(dexscreener_object, full_mats_list):

    dfk_mats_price_dictionary = dexscreener_object.wjewel_discovery_price_dictionary()

    for mat in full_mats_list:
        assert dfk_mats_price_dictionary.get(mat)
