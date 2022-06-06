from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup


storage = MemoryStorage()


#   States
class Form(StatesGroup):
    product_name = State()
    size = State()
    kilo = State()
    price_for_kilo = State()
    alive = State()
    delivery = State()
    coocked = State()
 
