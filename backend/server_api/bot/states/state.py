from aiogram.dispatcher.filters.state import StatesGroup, State


class SetLocation(StatesGroup):
    set_location = State()


class SetlocationWeather(StatesGroup):
    set_location_weather = State()


class SetlocationWeatherTwoDays(StatesGroup):

    set_location_weather = State()
    