from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text='Прогноз погоды' ,callback_data='weather_menu')
    button2 = InlineKeyboardButton(text='Дополнительные функции' ,callback_data='alert_menu')
    return keyboard.add(button1, button2)


def get_weather_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    show_weather = InlineKeyboardButton(
        text='Текущая погода', callback_data='show_weather')
    show_weather_48h = InlineKeyboardButton(
        text='Погода на 2 дня', callback_data='show_weather_48h')
    back_menu = InlineKeyboardButton(text='Назад', callback_data='back_menu')
    return keyboard.add(show_weather, show_weather_48h, back_menu)


back_menu_keyboard = InlineKeyboardMarkup()
back = InlineKeyboardButton(text='Назад', callback_data='back_weather_menu')
back_menu_keyboard.add(back)


def get_keyboard_from_show_weather(address):
    keyboard = InlineKeyboardMarkup(row_width=1)
    custom_adr = InlineKeyboardButton(text=f'{address}', callback_data='custom_address')
    new_adr = InlineKeyboardButton(text='новый адрес', callback_data='new_address')
    return keyboard.add(new_adr, custom_adr)


def get_keyboard_from_show_weather_48h(address):
    keyboard = InlineKeyboardMarkup(row_width=1)
    custom_adr = InlineKeyboardButton(
        text=f'{address}', callback_data='custom_address_48h')
    new_adr = InlineKeyboardButton(
        text='новый адрес', callback_data='new_address_48h')
    return keyboard.add(new_adr, custom_adr)


def get_subscriber_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text='Предупреждать об осадках', callback_data='alert_weather')
    # button2 = InlineKeyboardButton(text='Прогноз погоды по расписанию', callback_data='#')
    back_menu = InlineKeyboardButton(text='Назад', callback_data='back_menu')
    return keyboard.add(button1, back_menu)


def get_change_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text='Да', callback_data='yes')
    button2 = InlineKeyboardButton(text='Нет', callback_data='back_menu')
    return keyboard.add(button1, button2)


def get_delete_subscribe_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text='Отписаться', callback_data='delete_subscribe')
    button2 = InlineKeyboardButton(text='Назад', callback_data='back_menu')
    return keyboard.add(button1, button2)
