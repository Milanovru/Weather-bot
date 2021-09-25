import time
from asgiref.sync import sync_to_async


class ControlData():
    '''Класс для анализа входных данных из API'''
    weather_data_dict = {}

    @sync_to_async
    def control_weather_data_from_alert_message(self, weather_data, telegram_id, timer):
        '''Функция проверяет описание погоды с id пользователя и возвращает True или False, 
        в зависимости изменились ли данные у пользователя. Необходима для решения отсылать уведомление пользователю или нет'''
        if self.weather_data_dict.get(telegram_id):
            if self.weather_data_dict[telegram_id] != weather_data:
                self.weather_data_dict[telegram_id] = weather_data
                # если изменился тип осадков и прошло больше 2 часов
                if int(time.time()-timer) > 7200:
                    return True
                else:
                    return False
            else:
                # если после хорошей погоды наступает такой же вид плохих осадков и прошло больше 6 часов, вернуть True
                if int(time.time()-timer) > 7200:
                    return True
                else:
                    return False
        else:
            self.weather_data_dict[telegram_id] = weather_data
