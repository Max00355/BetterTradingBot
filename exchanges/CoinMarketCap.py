from exchanges.Wrapper import Wrapper
import config
import requests
import random

class CoinMarketCap(Wrapper):
    def __init__(self):
        Wrapper.__init__(self)
        self.funds_dict = {}
        self.API_URL = "https://api.coinmarketcap.com/v1/ticker/"
        self.usd = 1000
        self.buy_val = 0
        self.orig_price = 0

    def buy(self, worth):
        if worth == 0:
            return
        price = self.price()
        if worth <= self.usd:
            amount = float(worth) / price
            self.usd -= worth
            if config.BUY not in self.funds_dict:
                self.funds_dict[config.BUY] = 0
            self.funds_dict[config.BUY] += amount
            self.buy_val = price
        else:
            raise Exception("Insufficient funds")
    
    def sell(self, amount):
        if amount == 0:
            return
        if config.BUY not in self.funds_dict:
            raise Exception("Insufficient funds")

        if self.funds_dict[config.BUY] < amount:
            amount = self.funds_dict[config.BUY]

        price = self.price()       
        self.buy_val = price
        self.funds_dict[config.BUY] -= amount
        self.usd += amount * price
        
    def buy_value(self):
        return self.buy_val

    def funds(self):
        if config.BUY not in self.funds_dict:
            amount = 0
        else:
            amount = self.funds_dict[config.BUY]
        return {
                config.BUY:amount,
                "USD":self.usd
                }

    def price(self):
        if config.DEBUG:
            if not self.orig_price:
                api_data = requests.get(self.API_URL).json()
                for coin in api_data:
                    if coin['symbol'] == config.BUY.upper():
                        self.orig_price = float(coin['price_usd'])
            else:
                self.orig_price += (random.randint(0, 3) / 100.0) * self.orig_price * random.choice([1, -1])
        
            return self.orig_price
        else:
            api_data = requests.get(self.API_URL).json()
            for coin in api_data:
                if coin['symbol'] == config.BUY.upper():
                    return float(coin['price_usd'])

