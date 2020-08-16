from __future__ import annotations

from core.weather_provider import WeatherProviderInterface, Weather
from core.weather_providers.OpenWeatherMap import OpenWeatherMapInterface
from core.weather_providers.WeatherStack import WeatherStackInterface


class WeatherProviderManager:
    """
    Реализация менеджэра погодных провайдеров.
    """

    def __init__(self, config):
        """
        Инициализация менеджэра погодных провайдеров.
        :param dict config: Конфигурация погодных провайдеров.
        """
        self._providers = {"OpenWeatherMap": lambda: OpenWeatherMapInterface(config["OpenWeatherMap"]),
                           "WeatherStack": lambda: WeatherStackInterface(config["WeatherStack"])}

    def get_weather_for_city(self, provider_type, city) -> Weather:
        """
        Запрос у конкретного провайдера информации о погоде по городу.
        :param str provider_type: Используемый тип погодного провайдера.
        :param str city: Город, для которого необходимо запросить погоду.
        """
        print(f"[{provider_type}]: Запрашиваем погоду для города '{city}'")
        provider: WeatherProviderInterface = self._providers[provider_type]()
        try:
            return provider.get_weather_for_city(city)
        except BaseException as e:
            print(e)

