from handlers.users.commands import send_alert_messages
from config import scheduler


async def start_scheduler_send_alert_message():
    # replace_existing - после перезапуска не создается новая копия работы шедулера
    scheduler.add_job(send_alert_messages, 'interval',minutes=20, id='send_alert_message', replace_existing=True)
                     