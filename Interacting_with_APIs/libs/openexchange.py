""" Creating an API Client to communicate on behalf of the app to the API server"""
import requests
from cachetools import cached, TTLCache
""" Previously used functools but changed to cachetools.
1. import functools
2. using the functools to cache the `latest` function
3. lru = least recently used, and maxsize = how many elements can be stored in the cache
4. @functools.lru_cache(maxsize=2)

"""


class OpenExchangeClient:

    # This is the base url of the openexchange API for any and all endpoints.
    BASE_URL = "https://openexchangerates.org/api/"

    # This dunder function will make sure the client always takes the app_id before any other functions are called.
    def __init__(self, app_id):
        self.app_id = app_id

    # This will make a get request to the API's `latest` endpoint and return the latest exchange rates.
    # Making this a property as it doesn't take in any arguments ard also does not modify the original object at all.
    #  specifying ttl as 900 seconds so it is less than an hour.
    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    # This is the main function called from the app to convert currency based on the latest exchange rates
    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
