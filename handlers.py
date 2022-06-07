from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from state import Form
import logging
from validator import bool_valid, kilo_valid


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
        try:
            data['kilo'] = float(message.text)
        except ValueError as ex:
            await cancel_handler(message, state, ex)
        else:
            await Form.next()
            await message.reply('Введи стоимость(за кг)')


async def add_price(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price_for_kilo'] = float(message.text)
    await Form.next()
    await message.reply('Живой?(y/n)')

async def alive(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['alive'] = bool_valid(message.text)
    await Form.next()
    await message.reply('Доставка?(y/n)')


async def delivery(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['delivery'] = bool_valid(message.text)
    await Form.next()
    await message.reply('Приготовленный?(y/n)')


async def coocked(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['coocked'] = bool_valid(message.text)
    
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


async def cancel_handler(message:types.Message, state:FSMContext, ex=None):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    if ex != None:
        await message.reply('Не корректный ввод')
    await message.reply('Cancelled')


