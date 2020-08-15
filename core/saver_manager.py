from __future__ import annotations

from core.weather_saver import Weather, WeatherSaver
from core.weather_savers.json_saver import JsonWeatherSaver
from core.weather_savers.xml_saver import XmlWeatherSaver


class WeatherSaverManager:
    """
    Реализация мэнеджера погодных сэйверов.
    """

    def __init__(self, config):
        """
        Инициализация менеджэра погодных сэйверов.
        :param dict config: Конфигурация погодных сэйверов.
        """
        self._savers = {"json": lambda: JsonWeatherSaver(config["json"]["json_format"]),
                        "xml": lambda: XmlWeatherSaver(config["xml"]["xml_format"])}

    def save(self, weather: Weather, file_path, saver_type) -> Weather:
        """
        Сохранение информации о погоде.
        :param Weather weather: Погода для сохранения.
        :param str file_path: Путь сохранения файла.
        :param str saver_type: тип используемого сэйвера.
        """
        saver: WeatherSaver = self._savers[saver_type]()
        if weather:
            return saver.save(weather, file_path)

