from __future__ import annotations
from abc import ABC

from core.weather_saver import Weather, WeatherSaver
from core.weather_provider import WeatherProvider
from core.weather_savers.json_saver import JsonWeatherSaver
from core.weather_savers.xml_saver import XmlWeatherSaver


class WeatherSaverManager(ABC):
    def __init__(self, config):
        self._savers = {"json": lambda: JsonWeatherSaver(config["json_format"]),
                        "xml": lambda: XmlWeatherSaver(config["xml_format"])}

    def save(self, weather: Weather, file_path, saver_type) -> Weather:
        saver: WeatherSaver = self._savers[saver_type]()
        return saver.save(weather, file_path)

