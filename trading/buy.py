import random
from config import RANDOM_MIN
import config
import math
import sys

def buy_random(api_obj, funds):
    unused_funds = funds[config.WITH]
    coins_owned = funds[config.BUY]

    if unused_funds < 1:
        buy_amount = unused_funds
    else:
        if unused_funds > RANDOM_MIN:
            buy_amount = random.randint(RANDOM_MIN, math.floor(unused_funds))
            api_obj.buy(buy_amount)
            print("Bought", buy_amount, config.WITH, "of", config.BUY, "({})".format(float(buy_amount) / api_obj.price()))
        elif coins_owned == 0:
            sys.exit("I've run out of funds")
