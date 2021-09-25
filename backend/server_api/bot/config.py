from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env
from utils import yandexapi, openweatherapi, controldata
from apscheduler.schedulers.asyncio import AsyncIOScheduler


env = Env()
env.read_env()

bot = Bot(token=env('BOT_TOKEN'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
yandex = yandexapi.YandexApi()
weather = openweatherapi.OpenweatherApi()
control_data = controldata.ControlData()
scheduler = AsyncIOScheduler()
