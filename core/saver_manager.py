from __future__ import annotations

from core.weather_saver import Weather, WeatherSaverInterface
from core.weather_savers.json_saver import JsonWeatherSaverInterface
from core.weather_savers.xml_saver import XmlWeatherSaverInterface


class WeatherSaverManager:
    """
    Реализация мэнеджера погодных сэйверов.
    """

    def __init__(self, config):
        """
        Инициализация менеджэра погодных сэйверов.
        :param dict config: Конфигурация погодных сэйверов.
        """
        self._savers = {"json": lambda: JsonWeatherSaverInterface(config["json"]["json_order"]),
                        "xml": lambda: XmlWeatherSaverInterface(config["xml"]["xml_order"])}

    def save(self, weather: Weather, file_path, saver_type) -> Weather:
        """
        Сохранение информации о погоде.
        :param Weather weather: Погода для сохранения.
        :param str file_path: Путь сохранения файла.
        :param str saver_type: тип используемого сэйвера.
        """
        print(f"[Saver:{saver_type}]: Сохраняем информацию о погоде...")
        saver: WeatherSaverInterface = self._savers[saver_type]()
        try:
            saver.save(weather, file_path)
        except BaseException as e:
            print(f"[Saver:{saver_type}]: ! ERROR: {e}")
        else:
            print(f"[Saver:{saver_type}]: > {file_path}")

