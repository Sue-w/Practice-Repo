from libs.openexchange import OpenExchangeClient

APP_ID = "62c231f6e99247de89d328ee6edb0b7a"
client = OpenExchangeClient(APP_ID)


usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f" {usd_amount} is equal to £{gbp_amount:.2f} in England")
