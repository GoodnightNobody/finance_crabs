import logging
from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN
from handlers import add_size, welcome, start_state, add_product_name, add_kilo, add_price, alive, delivery, coocked, cancel_handler
from state import storage, Form
from aiogram.dispatcher.filters import Text


# Configure logging
logging.basicConfig(level=logging.INFO)

# Init bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


# Регестрация хендлеров
dp.register_message_handler(welcome, commands=['start'])
dp.register_message_handler(start_state, commands=['addProduct'], state=None)
dp.register_message_handler(add_product_name, content_types=['text'], state=Form.product_name)
dp.register_message_handler(add_size, content_types=['text'], state=Form.size)
dp.register_message_handler(add_kilo, content_types=['text'], state=Form.kilo)
dp.register_message_handler(add_price, content_types=['text'], state=Form.price_for_kilo)
dp.register_message_handler(alive, content_types=['text'], state=Form.alive)
dp.register_message_handler(delivery, content_types=['text'], state=Form.delivery)
dp.register_message_handler(coocked, content_types=['text'], state=Form.coocked)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(Text(equals='cancel', ignore_case=True), state='*')


if __name__ == '__main__':
    executor.start_polling(dp)
