from requests import get

from core.weather import Weather
from core.weather_provider import WeatherProvider


class WeatherStack(WeatherProvider):
    """
    Реализация погодного провайдера.
    https://weatherstack.com/
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
        """
        Приведение ответа WeatherStack к единному формату для хранения погоды.
        :param dict weather: Ответ от WeatherStack.
        """
        formated_weather = \
            {
                "temp": float(weather["current"]["temperature"]),
                "feels_like": float(weather["current"]["feelslike"]),
                "pressure": weather["current"]["pressure"],
                "humidity": weather["current"]["humidity"],
                "visibility": weather["current"]["visibility"]*1000,
                "cloudcover": weather["current"]["cloudcover"],

                "location": {
                    "name": weather["location"]["name"],
                    "coord": {
                        "lon": float(weather["location"]["lon"]),
                        "lat": float(weather["location"]["lat"])
                    }
                },
                "wind": {
                    "speed": weather["current"]["wind_speed"],
                    "deg": weather["current"]["wind_degree"]
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
        # Формат запроса: "http://api.weatherstack.com/current?query={}&access_key={}&units=m"
        req_url = self.__url.format(city, self.__api_key)

        # ToDo: обработка результатов запроса (если не 200, то выдумывать)
        weather_response = get(req_url).json()

        return self._weather_translator(weather_response)
