from exchanges.Wrapper import Wrapper
import config
import requests

class CoinMarketCap(Wrapper):
    def __init__(self):
        Wrapper.__init__(self)
        self.funds_dict = {}
        self.API_URL = "https://api.coinmarketcap.com/v1/ticker/"
        self.usd = 1000
        self.buy_val = 0

    def buy(self, worth):
        price = self.price()
        if worth <= self.usd:
            amount = float(worth) / price
            self.usd -= worth
            if config.BUY not in self.funds_dict:
                self.funds_dict[config.BUY] = 0
            self.funds_dict[config.BUY] += amount
            self.buy_val = worth
        else:
            raise Exception("Insufficient funds")
    
    def sell(self, amount):
        if config.BUY not in self.funds_dict or self.funds_dict[config.BUY] < amount:
            raise Exception("Insufficient funds")
        
        self.funds_dict[config.BUY] -= amount
        self.usd += amount * self.price() + 500
   
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
        api_data = requests.get(self.API_URL).json()
        for coin in api_data:
            if coin['symbol'] == config.BUY.upper():
                return float(coin['price_usd'])
