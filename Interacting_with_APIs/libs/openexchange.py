""" Creating an API Client to communicate on behalf of the app to the API server"""

import requests


class OpenExchangeClient:

    # This is the base url of the openexchange API for any and all endpoints.
    BASE_URL = "https://openexchangerates.org/api/"

    # This dunder function will make sure the client always takes the app_id before any other functions are called.
    def __init__(self, app_id):
        self.app_id = app_id

    # This will make a get request to the API's `latest` endpoint and return the latest exchange rates.
    # Making this a property as it doesn't take in any arguments ard also does not modify the original object at all.
    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    # This is the main function called from the app to convert currency based on the latest exchange rates
    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
