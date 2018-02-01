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
  a. If appreciated by more than config.WITHDRAW_PROFITS_AT then sell the difference
  b. If depreciated in value more than config.SELL_AT then sell everything and wait three hours before investing random amount again

"""


def main_loop(api_obj):
    if config.DEBUG:
        print("Press Enter to Continue")
    while True:
        funds = api_obj.funds()
        price = api_obj.price()
        
        buy_value = api_obj.buy_value()
        current_value = funds[config.BUY] * price
        value_percentage = check_value(funds, buy_value, price)
        buy = funds[config.BUY]
        unused = funds[config.WITH]

        print(config.WITH, funds[config.WITH])
        print(config.BUY, funds[config.BUY])
        print(config.BUY, "price", price)
        print("BUY PRICE({})".format(config.WITH), buy_value)
        print(str(round(100 * value_percentage, 2)) + "%", "change")
        print()
        if config.DEBUG:
            input()


        if config.BUY not in funds or not funds[config.BUY]:
            buy_random(api_obj, funds)
        else:
            if value_percentage < config.SELL_ALL_AT:
                sell_all(api_obj, funds)
                if not config.DEBUG:
                    time.sleep(60 * 60 * 6)
            elif value_percentage > config.WITHDRAW_PROFITS_AT:
                sell_profits(api_obj, price, buy_value, funds)

       
        if not config.DEBUG:
            time.sleep(60)
