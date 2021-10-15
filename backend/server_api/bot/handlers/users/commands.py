from config import dp, bot, env, weather, control_data
from aiogram.types import Message
from aiogram import types
from keyboards.inline import get_weather_keyboard, get_subscriber_keyboard, get_menu_keyboard
from server_api.bot.utils.db_commands import *
import aiogram
from loguru import logger
import time


@dp.message_handler(commands='start')
async def hello(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}.\nВведи /menu для продолжения')
 

@dp.message_handler(commands='menu')
async def get_menu(message: Message):
    await message.answer('Меню погоды', reply_markup=get_menu_keyboard())


@dp.message_handler(commands='weather')
async def get_menu(message: Message):
    await message.answer('Меню погоды', reply_markup=get_weather_keyboard())


@dp.message_handler(commands='functions')
async def get_menu(message: Message):
    await message.answer('Меню дополнительных функций', reply_markup=get_subscriber_keyboard())


# этот хендлер задает дефолтный список команд
@dp.message_handler(commands="set_commands", state="*", user_id=env('ADMIN'))
async def cmd_set_commands(message: Message):
    commands = [types.BotCommand(command="/menu", description="Главное меню"),
    types.BotCommand(command="/weather", description="Меню погоды"),
    types.BotCommand(command='/functions', description='Меню функций')
    ]
    await bot.set_my_commands(commands)
    await message.answer('Изменения внесены')


async def send_alert_messages():
    subscribers = await get_all_subscribers()
    for subscriber in subscribers:
        id = subscriber[0]
        lat = subscriber[1]
        lon = subscriber[2]
        weather_description = await weather.get_alert_weather(lat, lon)
        if weather_description is not None:
            if await control_data.control_weather_data_from_alert_message(weather_description, id, time.time()):
                try:
                    await bot.send_message(id, f'По твоему адресу ожидается {weather_description}')
                except aiogram.utils.exceptions.ChatNotFound as e:
                    logger.error(f'{e}\nОшибка в функции commands.send_alert_messages')
