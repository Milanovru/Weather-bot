import requests
from environs import Env
from loguru import logger


class YandexApi():
    '''Работает с API https://geocode-maps.yandex.ru'''
    env = Env()
    env.read_env()

    token = env('YANDEX_KEY')
    
    async def get_address(self,locate):
        '''Возвращает строку с адресом на основании переданной локации пользователем'''
        params = {"apikey": self.token,
            "format": "json",
            "lang": "ru_RU",
            "kind": "house",
                "geocode": locate}
        try:
            r = requests.get(
                url="https://geocode-maps.yandex.ru/1.x/", params=params)
            #получаем данные
            json_data = r.json()
            #вытаскиваем из всего пришедшего json именно строку с полным адресом.
            address_str = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                "metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
            return address_str
        except Exception as e:
            logger.error(f'{e}\nОшибка при генерации адреса из API yandex')
            return 'error'
