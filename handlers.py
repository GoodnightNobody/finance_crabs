from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from state import Form
import logging


async def welcome(message:types.Message):
    await message.reply('Добро пожаловать. Не парься с финансами, я все сделаю за тебя.')
 
 

async def start_state(message:types.Message):
    await Form.product_name.set()
    await message.reply('Введи название продукта')


async def add_product_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text
    await Form.next()
    await message.reply('Теперь введи размер')


async def add_size(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await Form.next()
    await message.reply('Введи вес(кг)')


async def add_kilo(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['kilo'] = message.text
    await Form.next()
    await message.reply('Введи стоимость(за кг)')


async def add_price(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_for_kilo'] = message.text
    await Form.next()
    await message.reply('Живой?(y/n)')


async def alive(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['alive'] = message.text
    await Form.next()
    await message.reply('Доставка?(y/n)')


async def delivery(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['delivery'] = message.text
    await Form.next()
    await message.reply('Приготовленный?(y/n)')


async def coocked(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['coocked'] = message.text
    
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


async def cancel_handler(message:types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled')


