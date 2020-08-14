import requests

from core.weather import Weather
from core.weather_provider import WeatherProvider


class OpenWeatherMap(WeatherProvider):
    """
    Реализация погодного провайдера.
    https://openweathermap.org/
    """

    def __init__(self, config):
        """
        Инициализация погодного провайдера.
        Для запроса необходим api_key (выдается на аккаунт, необходима регистрация)
        :param dict config: Аргументы инициализации. Параметр должен содержать url запроса и api_key
        """
        super().__init__()
        self.__api_key = config["api_key"]
        self.__url = config["url"]

    def get_weather_for_city(self, city) -> Weather:
        """
        Получение погоды по заданному городу.
        Для запроса необходим api_key (выдается на аккаунт, необходима регистрация)
        :param str city: Город, для которого запросить погоду
        """

        # Формируем запрос
        # Формат запроса: http://api.openweathermap.org/data/2.5/weather?q={}&appid={}
        req_url = self.__url.format(city, self.__api_key)

        # ToDo: обработка результатов запроса (если не 200, то выдумывать)
        response = requests.request("GET", req_url)

        return Weather(response.json())
