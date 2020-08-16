from __future__ import annotations

from core.weather_provider import WeatherProvider, Weather
from core.weather_providers.OpenWeatherMap import OpenWeatherMap
from core.weather_providers.WeatherStack import WeatherStack


class WeatherProviderManager:
    """
    Реализация менеджэра погодных провайдеров.
    """

    def __init__(self, config):
        """
        Инициализация менеджэра погодных провайдеров.
        :param dict config: Конфигурация погодных провайдеров.
        """
        self._providers = {"OpenWeatherMap": lambda: OpenWeatherMap(config["OpenWeatherMap"]),
                           "WeatherStack": lambda: WeatherStack(config["WeatherStack"])}

    def get_weather_for_city(self, provider_type, city) -> Weather:
        """
        Запрос у конкретного провайдера информации о погоде по городу.
        :param str provider_type: Используемый тип погодного провайдера.
        :param str city: Город, для которого необходимо запросить погоду.
        """
        provider: WeatherProvider = self._providers[provider_type]()
        return provider.get_weather_for_city(city)

