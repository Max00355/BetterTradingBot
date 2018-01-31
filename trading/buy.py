import random
from config import RANDOM_MIN
import config
import math

def buy_random(api_obj, unused_funds):
    buy_amount = random.randint(RANDOM_MIN, math.floor(unused_funds)) 
    api_obj.buy(buy_amount)
    print("Bought", buy_amount, config.WITH, "of", config.BUY)
