from exchanges import Sandbox
import config
from trading.main_loop import main_loop

objects = {
    "sandbox":Sandbox.Sandbox,
}

api_obj = objects[config.EXCHANGE]

main_loop(api_obj)
