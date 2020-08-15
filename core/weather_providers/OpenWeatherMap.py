from requests import get
from collections import OrderedDict

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
        Для запроса необходим api_key (выдается на аккаунт, необходима регистрация).
        :param dict config: Аргументы инициализации. Параметр должен содержать url запроса и api_key.
        """
        super().__init__()
        self.__api_key = config["api_key"]
        self.__url = config["url"]

    def _weather_translator(self, weather: OrderedDict) -> Weather:
        """
        Приведение ответа OpenWeatherMap к единному формату для хранения погоды.
        :param OrderedDict weather: Ответ от OpenWeatherMap.
        """
        formated_weather = OrderedDict(
            date=weather["dt"],
            temp=weather["main"]["temp"],
            feels_like=weather["main"]["feels_like"],
            pressure=weather["main"]["pressure"],
            humidity=weather["main"]["humidity"],
            visibility=weather["visibility"],
            cloudcover=weather["clouds"]["all"],

            location_name=weather["name"],
            location_lon=weather["coord"]["lon"],
            location_lat=weather["coord"]["lat"],

            wind_speed=weather["wind"]["speed"],
            wind_deg=weather["wind"]["deg"]
        )
        return Weather(formated_weather)

    def get_weather_for_city(self, city) -> Weather:
        """
        Получение погоды по заданному городу.
        Для запроса необходим api_key (выдается на аккаунт, необходима регистрация).
        :param str city: Город, для которого запросить погоду.
        """

        # Формируем запрос
        # Формат запроса: http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric
        req_url = self.__url.format(city, self.__api_key)

        try:
            weather_response = get(req_url)

            if weather_response.status_code == 404:
                raise ValueError("Запрашиваемый Вами городород не найден.")
            if weather_response.status_code == 401:
                raise ValueError("Проблемы с авторизацией. Проверьте правильность api_key для OpenWeatherMap.")
        except ValueError as e:
            print(e)
            return None

        return self._weather_translator(weather_response.json())
