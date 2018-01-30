class Wrapper:
    def __init__(self):
        pass

    def buy(self, amount):
        """ 
        Buys amount of config.BUY for config.WITH
        """

        raise Exception("Must implement a buy method.")
    
    def sell(self, amount):
        """
        Sells amount of config.BUY for config.WIDTH
        """

        raise Exception("Must implement a sell method.")
    
    def funds(self):
        """
        Return Dict object of coin tickers and amount owned of each config.BUY and config.WITH
        """
        raise Exception("Must implement a funds method.")
    
    def price(self):
        """
        Returns float price of config.BUY
        """
        raise Exception("Must implement a price method.")
