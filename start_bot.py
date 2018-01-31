from exchanges import Sandbox, CoinMarketCap
import config
from trading.main_loop import main_loop

objects = {
    "sandbox":Sandbox.Sandbox,
    "coinmarketcap":CoinMarketCap.CoinMarketCap
}

api_obj = objects[config.EXCHANGE]()

main_loop(api_obj)
