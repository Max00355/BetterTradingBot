import config 
import time
import datetime
from trading.buy import buy_random
from trading.value import check_value
from trading.sell import sell_all, sell_profits
import random

"""
Algorithm Steps

1. Check amount owned
  a. If amount owned of config.BUY is zero then buy random amount
2. Check if value appreciated/depreciated in value
  a. If appreciated by more than config.WITHDRAW_PROFITS_AT then sell the difference and invest random amount again at new price
  b. If depreciated in value more than config.SELL_AT then sell everything and wait three hours before investing random amount again

"""


def main_loop(api_obj):
    print (' | '.join(["Date", config.BUY, config.WITH, "Price", "Bought At", "Value", "Value Percent Difference"]))
    while True:
        funds = api_obj.funds()
        unused_funds = funds[config.WITH.upper()]
        price = api_obj.price()
        
        if config.DEBUG:
            rand = random.randint(0, 100)
            if rand < 10:
                price -= 500
            elif rand > 90:
                price += 500
        
        buy_value = api_obj.buy_value()
        current_value = funds[config.BUY] * price
        value_percentage = check_value(funds, buy_value, price)
        buy = funds[config.BUY]
        unused = funds[config.WITH]
        print(datetime.datetime.now(), buy, unused, price, buy_value, current_value, str(value_percentage * 100) + "%" )
        
        if config.BUY not in funds or not funds[config.BUY]:
            buy_random(api_obj, unused_funds)
        else:
            if value_percentage < config.SELL_ALL_AT:
                sell_all(api_obj, funds)
            elif value_percentage > config.WITHDRAW_PROFITS_AT:
                sell_profits(api_obj, price, buy_value, funds)
    
        #time.sleep(2)
