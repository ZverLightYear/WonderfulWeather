from __future__ import annotations
from abc import abstractmethod, ABC

from core.weather_provider import WeatherProvider, Weather
from core.weather_providers.OpenWeatherMap import OpenWeatherMap
from core.weather_providers.WeatherStack import WeatherStack


class WeatherProviderManager(ABC):

    def __init__(self, config):
        self._providers = {"OpenWeatherMap": lambda: OpenWeatherMap(config["OpenWeatherMap"]),
                           "WeatherStack": lambda: WeatherStack(config["WeatherStack"])}

    def get_weather_for_city(self, provider_type, city) -> Weather:
        provider: WeatherProvider = self._providers[provider_type]()
        return provider.get_weather_for_city(city)

