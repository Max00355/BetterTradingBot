from trading.buy import buy_random
import config

def sell_all(api_obj, funds):
    api_obj.sell(funds[config.BUY])    
    print("Sold", funds[config.BUY], config.BUY)

def sell_profits(api_obj, price, buy_value, funds):
    current_value = funds[config.BUY] * price
    difference = current_value - buy_value
    amount = funds[config.BUY] / float(difference)
    api_obj.sell(amount)
    print("Sold", amount, config.BUY)
    buy_random(api_obj, funds)
