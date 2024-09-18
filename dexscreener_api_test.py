import pytest
import json
from pathlib import Path
from datetime import datetime, timedelta

from dexscreener_api import *

@pytest.fixture #Make sure a file exists at DexscreenerStaticValues.DEXSCREENER_DATABASE_FILEPATH or this fixture will cause an error!
def dexscreener_object():
    return DexscreenerDatabaseManager() 

@pytest.fixture
def full_mats_list():
    return DexscreenerStaticValues.FISH_LIST + DexscreenerStaticValues.PLANT_LIST + DexscreenerStaticValues.CRYSTAL_LIST + DexscreenerStaticValues.TEARS_AND_EGGS_LIST + DexscreenerStaticValues.CURRENCIES


@pytest.mark.skip #Only run this when your dexscreener_database_file is backed up. When this method is ran some 0xaddresses and prices may be missing because Dexscreener doesn't seem to have all mats at all times or days.
def test_initialize_dexscreener_dfk_mats_prices_json():
    json_database = Path(DexscreenerStaticValues.DEXSCREENER_DATABASE_FILEPATH)
    
    if json_database.is_file():
        json_database.unlink()

    database_generator = InitializeDexscreenerJsonDatabase()
    database_generator.initialize_dexscreener_dfk_mats_prices_json()

    assert json_database.is_file()


def test_json_pair_addresses(dexscreener_object, full_mats_list):
    for mat in full_mats_list:
        print(f"{mat}: dictionary.get(mat): {dexscreener_object.dexscreener_dfk_mats_dictionary.get(mat)}")
        assert dexscreener_object.dexscreener_dfk_mats_dictionary.get(mat).get("pair_address")[:2] == "0x"


def test_wjewel_native_prices(dexscreener_object, full_mats_list):
    for mat in full_mats_list:
        print(f"{mat}: dictionary.get(mat): {dexscreener_object.dexscreener_dfk_mats_dictionary.get(mat)}")
        assert float(dexscreener_object.dexscreener_dfk_mats_dictionary.get(mat).get("price_native")) > 0


def test_is_update_time(dexscreener_object):
    last_updated = dexscreener_object.dexscreener_dfk_mats_dictionary.get("last_updated")
    current_time = datetime.now()
    test_true_datetime = current_time - timedelta(hours=6)
    test_false_datetime = current_time - timedelta(hours=1)

    print(f"test_true_datetime_difference: {current_time - test_true_datetime}\ntest_false_datetime_difference: {current_time - test_false_datetime}\ndexscreener_object.is_update_time(): {dexscreener_object.is_update_time()}\n")

    dexscreener_object.dexscreener_dfk_mats_dictionary["last_updated"] = test_true_datetime.strftime(DexscreenerStaticValues.DATABASE_DATETIME_FORMAT) 
    print(f"After time update\ndexscreener_object.is_update_time(): {dexscreener_object.is_update_time()}")
    assert dexscreener_object.is_update_time()

    dexscreener_object.dexscreener_dfk_mats_dictionary["last_updated"] = test_false_datetime.strftime(DexscreenerStaticValues.DATABASE_DATETIME_FORMAT)
    assert not dexscreener_object.is_update_time()

    dexscreener_object.dexscreener_dfk_mats_dictionary["last_updated"] = last_updated

