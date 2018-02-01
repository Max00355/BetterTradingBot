import config

def sell_all(api_obj, funds):
    api_obj.sell(funds[config.BUY])    
    print("Sold", funds[config.BUY], config.BUY, "for", funds[config.BUY] * api_obj.price(), config.WITH)

def sell_profits(api_obj, price, buy_value, funds):
    current_value = funds[config.BUY] * price
    difference = current_value - (buy_value * funds[config.BUY])
    amount = funds[config.BUY] / float(difference)
    api_obj.sell(amount)
    print("Sold profits", amount, config.BUY, "for", amount * price, config.WITH)
