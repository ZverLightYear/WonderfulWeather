from requests import get

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

    def _weather_translator(self, weather: dict) -> Weather:
        formated_weather = \
            {
                "temp": weather["main"]["temp"],
                "feels_like": weather["main"]["feels_like"],
                "pressure": weather["main"]["pressure"],
                "humidity": weather["main"]["humidity"],
                "visibility": weather["visibility"],
                "cloudcover": weather["clouds"]["all"],

                "location": {
                    "name": weather["name"],
                    "coord": {
                        "lon": weather["coord"]["lon"],
                        "lat": weather["coord"]["lat"]
                    }
                },
                "wind": {
                    "speed": weather["wind"]["speed"],
                    "deg": weather["wind"]["deg"]
                }
            }
        return Weather(formated_weather)

    def get_weather_for_city(self, city) -> Weather:
        """
        Получение погоды по заданному городу.
        Для запроса необходим api_key (выдается на аккаунт, необходима регистрация).
        :param str city: Город, для которого запросить погоду.
        """

        # Формируем запрос
        # Формат запроса: http://api.openweathermap.org/data/2.5/weather?q={}&appid={}
        req_url = self.__url.format(city, self.__api_key)

        # ToDo: обработка результатов запроса (если не 200, то выдумывать)
        weather_response = get(req_url).json()

        return self._weather_translator(weather_response)
