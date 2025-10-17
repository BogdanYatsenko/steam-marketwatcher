# From PySteamMarket-master/steam_market/__init__.py
from .steam_market import *



# From PySteamMarket-master/steam_market/steam_market.py
import requests, urllib

'''
TODO:
  * add all currencies supported by the Steam Marketplace to `curAbbrev`
  * create docstrings for all functions
  * listings parser; get total number of listings (`total_count` in JSON)
  * get price overview via http://steamcommunity.com/market/priceoverview/
'''

class MarketListing:
    def __init__(self, listing_id, price):
        self._id = listing_id
        self.price = price

class MarketItem:
    def __init__(self, item_id=None, listings=None):
        self._id = item_id
        if listings:
            self.listings = listings
        else:
            self.listings = []

    def add_listing(self, l_id, price):
        self.listings.append(MarketListing(l_id, price))

# Currency abbreviations
curAbbrev = {
    'USD' : 1,
    'GBP' : 2,
    'EUR' : 3,
    'CHF' : 4,
    'RUB' : 5,
    'KRW' : 16,
    'CAD' : 20,
}

"""
Gets item listings from the Steam Marketplace.

@param game_id: ID of game item belongs to.
@param item: Name of item to lookup.
@param start: Listing index to start from. 0 is the most recent listing.
@param start: number >= 0
@param count: Number of listings to grab, start and beyond.
@param count: number >= 1
@param currency: Abbreviation of currency to return listing prices in.
@type currency:
    Accepted currencies:

      - USD
      - GBP
      - EUR
      - CHF
      - RUB
      - KRW
      - CAD

    Please lookup the proper abbreviation for your currency of choice.
@return A list of prices. Depending on your chosen currency, you may need to
    move the decimal place. For instance, in USD, $25.98 would be returned
    as 2598
"""
def get_item(game_id, item, start=0, count=10, currency='USD'):
    url = 'http://steamcommunity.com/market/listings/{}/{}/render'.format(
        game_id,
        urllib.parse.quote(item)
    )
    payload = {
        'start' : start,
        'count' : count,
        'currency' : curAbbrev[currency]
    }
    resp = requests.get(url, params=payload)
    listings = resp.json()['listinginfo']
    market_item = MarketItem()
    for l_id, v in listings.items():
        price = v['converted_price_per_unit'] + v['converted_fee_per_unit']
        market_item.add_listing(l_id, price)
    return market_item

def get_tf2_item(item, start=0, count=10, currency='USD'):
    return get_item('440', item, start, count)

def get_csgo_item(item, start=0, count=10, currency='USD'):
    return get_item('730', item, start, count)



# From PySteamMarket-master/tests/test_steam_market.py
#!/usr/bin/env python3

import unittest
import steam_market as sm

class TestTF2Items(unittest.TestCase):
    def runTest(self):
        tf2_items = [
            'Strange Professional Killstreak Minigun',
            'Vintage Gunboats',
            'Name Tag',
            'Mann Co. Supply Crate Key'
        ]

        csgo_items = [
            'Gamma Case',
            '\u2605 Karambit | Bright Water (Factory New)',
            'AK-47 | Frontside Misty (Field-Tested)'
        ]

        print('Testing TF2 Items:\n')
        for item in tf2_items:
            print(item)
            market_item = sm.get_tf2_item(item)
            print([i.price for i in market_item.listings])

        print('\nTesting CS:GO Items:\n')
        for item in csgo_items:
            print(item)
            market_item = sm.get_csgo_item(item)
            print([i.price for i in market_item.listings])

