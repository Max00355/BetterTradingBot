class Wrapper:
    def __init__(self):
        pass

    def buy(self, amount):
        """ 
        Buys amount of config.BUY for amount which is in config.WITH

        If insufficient funds then raise Exception("Insufficient funds")
        """

        raise Exception("Must implement a buy method.")
    
    def sell(self, amount):
        """
        Sells amount of config.BUY for config.WITH

        If insufficient funds then raise Exception("Insufficient funds")
        """

        raise Exception("Must implement a sell method.")

    def buy_value(self):
        """
        Returns the value of config.BUY at the time of buying.

        This value may need to be saved locally depending on the exchange.
        """

        raise Exception("Must implement buy_price.")

    def funds(self):
        """
        Return Dict object of coin tickers and amount owned of each config.BUY and config.WITH
        """
        raise Exception("Must implement a funds method.")
    
    def price(self):
        """
        Returns float price of config.BUY in USD or USDT
        """
        raise Exception("Must implement a price method.")
