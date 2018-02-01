import random
from config import RANDOM_MIN
import config
import math
import sys

def buy_all(api_obj, funds):
    unused_funds = funds[config.WITH]
    coins_owned = funds[config.BUY]
    buy_amount = unused_funds
    api_obj.buy(buy_amount)
    print("Bought", buy_amount, config.WITH, "of", config.BUY, "({})".format(float(buy_amount) / api_obj.price()))
