from server_api.models import Location, Subscriber, Address, IsSubscribed
from asgiref.sync import  sync_to_async
from loguru import logger


@sync_to_async
def create_location(lon, lat):
    '''Создаёт объект в таблице Location'''
    try:
        location = Location.objects.update_or_create(longitude=lon, latitude=lat)
    except Exception as e:
        logger.error(f'{e}\nОшибка при созданни локации')

@sync_to_async
def get_location(lon, lat):
    '''Получает объект по атрибутам lon, lat из таблицы Location'''
    query = Location.objects.get(longitude=lon, latitude=lat)
    return query

@sync_to_async
def get_subscriber(telegram_id):
    '''Получает объект по telegram_id из таблицы Subscriber'''
    query = Subscriber.objects.get(id=telegram_id)
    return query

@sync_to_async
def check_subscriber(telegram_name):
    '''Получает объект по полю Subscriber.name из таблицы Location'''
    try:
        query = Location.objects.select_related().filter(subscriber__name=telegram_name)[0]
        return query
    except Exception as e:
        logger.error(f'{e}\nОшибка при получении объекта Location по полю Subscriber.{telegram_name}')

@sync_to_async
def update_subscriber_location_id(telegram_name, id):
    '''Обновляет поле Subscriber.locations при изменении Location.id у координат'''
    try:
        Subscriber.objects.filter(name=telegram_name).update(
            locations=Location.objects.get(id=id))
    except Exception as e:
        logger.error(f'{e}\nОшибка при обновлении локации у пользователя')

@sync_to_async
def create_subscriber(telegram_id, telegram_name):
    '''Создает объект в таблице Subscriber'''
    try:
        subscriber = Subscriber.objects.update_or_create(id=telegram_id,name=telegram_name)
        logger.info(f'Зарегистрирован новый пользвотель: {subscriber}')
    except Exception as e:
        logger.error(f'{e}\nОшибка при созданни пользователя')

@sync_to_async
def create_address(addr, locations_id):
    '''Создает объект в таблице Address на основании Location.id.
    Если address.id не привязан к пользователю - удаляет запись'''
    try:
        address = Address.objects.update_or_create(
            address=addr, locations=Location.objects.get(id=locations_id))
    except Exception as e:
        # удаление пустых координат
        delete_address = Location.objects.get(id=(Location.objects.last().id - 1)) 
        delete_address.delete()
        logger.error(f'{e}\nОшибка при созданни адреса')

@sync_to_async
def add_subscribe(subscriber):
    '''Добавляет запись в таблицу IsSubscribed, когда пользователь вызвал функцию sheduler.add_job'''
    try:
        IsSubscribed.objects.create(id=subscriber, is_subscribed=True)
        logger.info(f'{subscriber.name} оформил подписку на отслеживание плохих осадков')
    except Exception as e:
        logger.error(f'{e}\nОшибка при оформлении подписки')

@sync_to_async
def check_subscribe(subscriber):
    '''Проверяет статус подписки из таблицы IsSubscribed'''
    try:
        query = IsSubscribed.objects.filter(
            id=subscriber, is_subscribed='True').exists()
        if query:
            return True
    except Exception as e:
        logger.error(f'{e}\nОшибка при запросе статуса подписки')

@sync_to_async
def delete_subscribe(subscriber):
    '''Удаляет запись из таблицы IsSubscribed, когда пользователь вызвал функцию sheduler.delete_job'''
    try:
        query = IsSubscribed.objects.get(id=subscriber)
        query.delete()
    except Exception as e:
        logger.error(f'{e}\nОшибка при удалени подписки')


@sync_to_async
def get_all_subscribers():
    '''Выводит всех пользователей, которые подписаны на рассылку. Возвращает список кортежей с id и координатами пользователей'''
    query = IsSubscribed.objects.all()
    subscribers_list = []
    for q in query:
        id = q.id.id
        lat = q.id.locations.latitude
        lon = q.id.locations.longitude
        subscribers_list.append((id, lat, lon))
    return subscribers_list
