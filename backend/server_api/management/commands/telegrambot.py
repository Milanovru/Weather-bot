from django.core.management.base import BaseCommand
import sys
sys.path.append(
    '/Users/pavel_milanov/Desktop/programming/mpweather-bot/backend/server_api/bot')
from server_api.bot.loader import start_bot


class Command(BaseCommand):
    help = 'Starting bot'

    def handle(self, *args, **options):
        
        start_bot()
