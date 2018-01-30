from exchanges.Wrapper import Wrapper
import config
import requests

class Sandbox(Wrapper):
    def __init__(self):
        Wrapper.__init__(self)
        self.api_key = config.SANDBOX
    def buy(self, amount):
        pass
    def sell(self, amount):
        pass
    def funds(self):
        pass
    def price(self):
        pass
