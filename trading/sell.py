import config

def sell_all(api_obj, funds):
    api_obj.sell(funds[config.BUY])    
    print("Sold", funds[config.BUY], config.BUY, "for", funds[config.BUY] * api_obj.price(), config.WITH)

def sell_profits(api_obj, price, buy_value, funds):
    amount = funds[config.BUY] * config.SELL_PERCENTAGE
    api_obj.sell(amount)
    print("Sold profits", amount, config.BUY, "for", amount * price, config.WITH)
