import requests

APP_ID = "62c231f6e99247de89d328ee6edb0b7a"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()["rates"]

usd_amount = 1000
gbp_amount = 1000 * exchange_rates["GBP"]

print(f" ${usd_amount} is equal to £{gbp_amount} in England")
