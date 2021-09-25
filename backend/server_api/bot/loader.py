import  handlers
from config import dp, scheduler
from aiogram import executor
from loguru import logger
from utils.schedule_commands import start_scheduler_send_alert_message

async def on_startup(dp):
    scheduler.start()
    logger.add('debug/logs.log', format='{time} {level} {message}', level='DEBUG', rotation="100 KB", compression="zip")
    logger.info("Starting bot")
    # возобновляет подписки, если бот перезапускался
    await start_scheduler_send_alert_message()

def start_bot():
    executor.start_polling(dp, on_startup=on_startup)


if __name__ == "__main__":
     start_bot()
     