from config import dp, yandex, weather
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from keyboards.default import location_keyboard
from keyboards.inline import *
from states.state import *
from server_api.bot.utils.db_commands import *
from server_api.bot.utils.schedule_commands import *


@dp.callback_query_handler(text='no')
@dp.callback_query_handler(text='back_menu')
async def back_to_menu(call: CallbackQuery):
    await call.answer('Меню')
    await call.message.edit_reply_markup(reply_markup=get_menu_keyboard())


@dp.callback_query_handler(text='weather_menu')
async def get_keyboard(call: CallbackQuery):
    await call.answer('Меню погоды')
    await call.message.edit_reply_markup(reply_markup=get_weather_keyboard())


@dp.callback_query_handler(text='alert_menu')
async def get_keyboard(call: CallbackQuery):
    await call.answer('Меню дополнительных функций')
    await call.message.edit_reply_markup(reply_markup=get_subscriber_keyboard())


@dp.callback_query_handler(text='show_weather')
async def show_weather(call: CallbackQuery):
    await call.answer(cache_time=5)
    query = await check_subscriber(call.from_user.full_name)
    if query is None:
        await call.message.answer('Отправь свою локацию',
                                  reply_markup=location_keyboard)
        await create_subscriber(call.from_user.id, call.from_user.full_name)
        await SetlocationWeather.first()
    else:
        # если в БД есть данные, предлагаем пользоватю клавиатуру с последним адресом или выбором нового
        lon = query.longitude
        lat = query.latitude
        locate = (str(lon) + ' ' + str(lat))
        address = await yandex.get_address(locate)
        await create_address(address, query.id)
        await call.message.answer('где показать погоду?', reply_markup=get_keyboard_from_show_weather(address))


@dp.callback_query_handler(text="custom_address")
async def get_locate(call: CallbackQuery):
    await call.answer(cache_time=5)
    query = await check_subscriber(call.from_user.full_name)
    data = await weather.get_weather(query.longitude, query.latitude)
    await call.message.reply('Готово', reply_markup=ReplyKeyboardRemove())
    await call.message.answer_photo(photo=f"http://openweathermap.org/img/wn/{data.get('icon_weather')}@2x.png", caption=f'''
<b>Дата:</b> {data.get('day')} {data.get('mon')}
<b>Время:</b> {data.get('current_time')}
<b>Температура:</b> {data.get('temperature')} ℃
<b>Ощущается:</b> {data.get('feels_like_temperature')} ℃
<b>Влажность:</b> {data.get('humidity')} %
<b>Скорость ветра:</b> {data.get('wind_speed')} м/c
<b>Восход солнца:</b> {data.get('sunrise_time')}
<b>Закат солнца:</b> {data.get('sunset_time')}
''', reply_markup=back_menu_keyboard)


@dp.callback_query_handler(text='new_address')
async def show_locate(call: CallbackQuery):
    await call.answer('Определение местоположения')
    await call.message.answer('Отправь свою локацию',
                                  reply_markup=location_keyboard)
    await SetlocationWeather.first()


@dp.message_handler(state=SetlocationWeather.set_location_weather, content_types=ContentType.LOCATION)
async def get_locate(message: Message, state: FSMContext):
    lon = message.location.longitude
    lat = message.location.latitude
    await create_location(lon, lat)
    query = await get_location(lon, lat)
    await update_subscriber_location_id(message.from_user.full_name, query.id)
    data = await weather.get_weather(lat, lon)
    await state.finish()
    await message.reply('Готово', reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo=f"http://openweathermap.org/img/wn/{data.get('icon_weather')}@2x.png", caption=f'''
<b>Дата:</b> {data.get('day')} {data.get('mon')}
<b>Время:</b> {data.get('current_time')}
<b>Температура:</b> {data.get('temperature')} ℃
<b>Ощущается:</b> {data.get('feels_like_temperature')} ℃
<b>Влажность:</b> {data.get('humidity')} %
<b>Скорость ветра:</b> {data.get('wind_speed')} м/c
<b>Восход солнца:</b> {data.get('sunrise_time')}
<b>Закат солнца:</b> {data.get('sunset_time')}
''', reply_markup=back_menu_keyboard)
                      

@dp.callback_query_handler(text='back_weather_menu')
async def back_to_menu(call: CallbackQuery):
    await call.answer('меню')
    await call.message.edit_reply_markup(reply_markup=get_weather_keyboard())


@dp.callback_query_handler(text='show_weather_48h')
async def show_weather(call: CallbackQuery):
    await call.answer(cache_time=5)
    query = await check_subscriber(call.from_user.full_name)
    if query is None:
        await call.message.answer(
        'Отправь свою локацию',
        reply_markup=location_keyboard)
        await create_subscriber(call.from_user.id, call.from_user.full_name)
        await SetlocationWeatherTwoDays.first()
    else:
        lon = query.longitude
        lat = query.latitude
        locate = (lon + ' ' + lat)
        address = await yandex.get_address(locate)
        await create_address(address, query.id)
        await call.message.answer('где показать погоду?', reply_markup=get_keyboard_from_show_weather_48h(address))


@dp.callback_query_handler(text='new_address_48h')
async def show_locate(call: CallbackQuery):
    await call.answer('Определение местоположения')
    await call.message.answer('Отправь свою локацию',
                              reply_markup=location_keyboard)
    await SetlocationWeatherTwoDays.first()


@dp.message_handler(state=SetlocationWeatherTwoDays.set_location_weather, content_types=ContentType.LOCATION)
async def get_locate(message: Message, state: FSMContext):
    lon = message.location.longitude
    lat = message.location.latitude
    await create_location(lon, lat)
    query = await get_location(lon, lat)
    await update_subscriber_location_id(message.from_user.full_name, query.id)
    data = await weather.get_weather_48h(lat, lon)
    await state.finish()
    await message.reply('Готово', reply_markup=ReplyKeyboardRemove())
    await message.answer('\n'.join(data), reply_markup=back_menu_keyboard)


@dp.callback_query_handler(text="custom_address_48h")
async def get_locate(call: CallbackQuery):
    await call.answer(cache_time=5)
    query = await check_subscriber(call.from_user.full_name)
    data = await weather.get_weather_48h(query.latitude, query.longitude)
    await call.message.reply('Готово', reply_markup=ReplyKeyboardRemove())
    await call.message.answer('\n'.join(data), reply_markup=back_menu_keyboard)


@dp.callback_query_handler(text='alert_weather')
async def alert_weather(call: CallbackQuery):
    await call.answer(cache_time=5)
    query = await check_subscribe(call.from_user.id)
    if query:
        await call.message.answer('подписка уже оформлена', reply_markup=get_delete_subscribe_keyboard())
    else:
        await call.message.answer(
            'При вкллючении этой функции я начну отслеживать осадки и буду предупреждать тебя, отправив уведобмление в чат.\nВключить?', 
            reply_markup=get_change_keyboard())


@dp.callback_query_handler(text='yes')
async def subscribe_menu(call: CallbackQuery):
    await call.answer(cache_time=5)
    subscriber = await get_subscriber(call.from_user.id) 
    await add_subscribe(subscriber)
    await start_scheduler_send_alert_message()
    await call.message.answer('Подписка оформлена', reply_markup=get_menu_keyboard())


@dp.callback_query_handler(text='delete_subscribe')
async def delete(call: CallbackQuery):
    await call.answer(cache_time=5)
    await delete_subscribe(call.from_user.id)
    await call.message.answer('Вы отписаны', reply_markup=get_menu_keyboard())


@dp.callback_query_handler(text='registration-web')
async def registration(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(f'Логин для регистрации: {call.from_user.id}', reply_markup=back_menu_keyboard)
