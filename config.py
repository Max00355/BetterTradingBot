# Debug

DEBUG = True # When set to true random the price will change at random time simulating big drops and gains. This is to test selling and buying and will cause loss in production.
BREAK_POINTS = True # Makes the program wait for enter key after every main_loop iteration
STARTING_AMOUNT = 1000 # USD

# API KEYS

POLONIEX = ""
SANDBOX = ""


# Trading Configurations

EXCHANGE = "coinmarketcap"

BUY = "BTC"
WITH = "USD"
SELL_ALL_AT = -0.05 # 5%
WITHDRAW_PROFITS_AT = 0.1 # 10%
SELL_PERCENTAGE = 0.1 # Sell 10% of profits when 5% increase occurs
RANDOM_MIN = 100
