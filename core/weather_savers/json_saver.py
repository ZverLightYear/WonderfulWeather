from collections import OrderedDict

from core.weather import Weather
from core.weather_saver import WeatherSaver


class JsonWeatherSaver(WeatherSaver):
    """
    Реализация сэйвера данных о погоде в формате JSON.
    """

    def __init__(self, saver_format):
        """
        Инициализация сэйвера данных.
        :param saver_format: Формат вывода данных о погоде.
        """
        self.__format = saver_format

    def _format_weather(self, weather: Weather):
        """
        Приведение информации о погоде к требуемому сэйвером формату.
        :param Weather weather: Информация о погоде, полученная от погодного провайдера.
        """
        try:
            return Weather(OrderedDict([(key, weather[key]) for key in self.__format]))
        except KeyError as ke:
            raise KeyError(f"Неизвестный элемент {ke}. Проверьте правильность полей в формате сохранения файла.")

    def save(self, weather: Weather, file_name: str):
        """
        Сохранение в файл информации о погоде в требуемом формате.
        :param Weather weather: Информация о погоде, полученная от погодного провайдера.
        :param str file_name: Путь сохранения файла.
        """
        formated_weather = self._format_weather(weather)

        with open(file_name, "w") as out:
            # контейнер с погодой изначально хранит всю информацию в JSON формате
            out.write(formated_weather.json())
