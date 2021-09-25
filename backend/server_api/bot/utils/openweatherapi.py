import requests
from environs import Env
import time


class OpenweatherApi():
    '''Класс работает с API https://openweathermap.org'''
    env = Env()
    env.read_env()

    token = env('OPENWEATHER_KEY')

    
    async def get_weather(self, lat, lon):
        '''Функция возвращает словарь data с данными на текущий момент, полученными при отправке локации пользователем'''
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.token}&units=metric')
        json_data = r.json()
        mon = self.__replace_month(time.gmtime(json_data['sys']['sunrise'])[1])
        data = {
            'main_weather': json_data['weather'][0]['main'],
            'description_weather': json_data['weather'][0]['description'],
            'icon_weather': json_data['weather'][0]['icon'],
            'temperature' : json_data['main']['temp'],
            'feels_like_temperature' : json_data['main']['feels_like'],
            'humidity' : json_data['main']['humidity'],
            'wind_speed' : json_data['wind']['speed'],
            'year': time.gmtime(json_data['sys']['sunrise'])[0],
            'mon': mon,
            'day' : time.gmtime(json_data['sys']['sunrise'])[2],
            'sunrise_time' : str(time.gmtime(json_data['sys']['sunrise'])[
                            3] + 3) + ':' + str(time.gmtime(json_data['sys']['sunrise'])[4]),
            'sunset_time' : str(time.gmtime(json_data['sys']['sunset'])[
                            3] + 3) + ':' + str(time.gmtime(json_data['sys']['sunset'])[4]),
            'current_time' : str(time.gmtime(time.time())[
                            3]+3) + ':' + str(time.gmtime(time.time())[4])
        }
        return data    
    
    
    async def get_weather_48h(self, lat, lon):
        '''Возвращает словарь data с данными на 48 часов, полученными при отправке локации пользователем'''
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily,alerts&appid={self.token}&units=metric')
        json_data = r.json()
        data = {
            'temp': [(i['temp']) for i in json_data['hourly']],
            'feels_like': [i['feels_like'] for i in json_data['hourly']],
            'main': [i['weather'][0]['main'] for i in json_data['hourly']],
            'description': [i['weather'][0]['description'] for i in json_data['hourly']],
            'mon': [self.__replace_month(time.gmtime(i['dt'])[1])for i in json_data['hourly']],
            'day': [time.gmtime(i['dt'])[2] for i in json_data['hourly']],
            'hour': [(time.gmtime(i['dt'])[3] + 3) for i in json_data['hourly']]
        }
        return self.__parse_mode_dict(data)

    
    async def get_alert_weather(self, lat, lon):
        '''Запускает функции отправки сообщений пользователям по расписанию.
        Принимает 3 аргумента: lat, lon - для запроса к API, telegram-id для передачи в функцию alert_messages'''
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={self.token}&units=metric&lang=ru')
        json_data = r.json()
        weather_id = str(json_data['current']['weather'][0]['id'])
        weather_description = json_data['current']['weather'][0]['description']
        # если погода == дождь, снег, гроза или сильный ветер - возвращаем предупреждение
        if weather_id.startswith('2') or weather_id.startswith('3') or weather_id.startswith('5') or weather_id.startswith('6') or weather_id.startswith('7'):
            return weather_description
            

    def __replace_month(self, month):
        if month == 1:
            return 'января'
        elif month == 2:
            return 'февраля'
        elif month == 3:
            return 'марта'
        elif month == 4:
            return 'апреля'
        elif month == 5:
            return 'мая'
        elif month == 6:
            return 'июня'
        elif month == 7:
            return 'июля'
        elif month == 8:
            return 'августа'
        elif month == 9:
            return 'сентября'
        elif month == 10:
            return 'октября'
        elif month == 11:
            return 'ноября'
        elif month == 12:
            return 'декабря'
        else:
            return None


    def __parse_mode_dict(self, data: dict):
        tmp = []
        day_tmp = None
        month_tmp = None
        for temp, month, day, hour, description, main in zip(
            data.get('temp'), data.get('mon'), data.get('day'), data.get('hour'), data.get('description'), data.get('main')
            ):
            unicode = self.__description_unicode(main, description)
            month_tmp = month
            day_tmp = day
            # не выводит дату для одного и того же дня
            if day == day_tmp and month == month_tmp:
                # когда наступает 00 часов
                if hour % 24 == 0:
                    s = f'<b>{day + 1}</b> <b>{month}</b>\n<b>{hour % 24}:00</b> {unicode} <b>{int(temp)}</b>℃'
                    tmp.append(s)
                # в течении дня
                else:
                    s = f'<b>{hour % 24}:00</b> {unicode} <b>{int(temp)}</b>℃'
                    month_tmp = month
                    day_tmp = day
                    tmp.append(s)
        return tmp


    def __description_unicode(self, group, subgroup):
        if group.lower() == 'thunderstorm':
            return '⛈️'
        elif group.lower() == 'drizzle':
            return '🌦'
        elif group.lower() == 'rain':
            return '🌧'
        elif group.lower() == 'snow':
            return '🌨'
        elif group.lower() == 'clear':
            return '☀'
        elif group.lower() == 'clouds':
            if subgroup.lower() == 'few clouds':
                return '🌤'
            elif subgroup.lower() == 'broken clouds':
                return '🌥'
            else:
                return '☁'
        else:
            return None
