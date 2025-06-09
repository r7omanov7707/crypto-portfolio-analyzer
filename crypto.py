import requests

coins = input("Enter coins (space-separated, e.g., bitcoin,  ethereum): ").lower().split()
portfolio = {}
for coin in coins:
    amount = float(input(f"How many {coin} do you own?: "))
    portfolio[coin] = amount

response = requests.get("https://api.coingecko.com/api/v3/simple/price",
                        params={"ids": ','.join(coins), "vs_currencies": "usd"})
prices = response.json()

total_value = 0
for coin, amount in portfolio.items():
    price = prices[coin]["usd"]
    value = price * amount
    total_value += value
    print(f"{coin.capitalize()}: {amount} x ${price:.2f} = ${value:.2f}")

print(f"\nTotal portfolio value: ${total_value:.2f}")
