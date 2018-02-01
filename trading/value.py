import config

def check_value(funds, buy_value, price):
    current_value = funds[config.BUY] * price
    difference = current_value - (buy_value * funds[config.BUY])
    try:
        percentage = difference / float(current_value)
    except ZeroDivisionError:
        percentage = 0
    
    return percentage
