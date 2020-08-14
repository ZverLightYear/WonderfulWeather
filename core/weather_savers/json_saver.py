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
        self.__format = reversed(saver_format)

    def _format_weather(self, weather: Weather):
        """
        Приведение информации о погоде к требуемому сэйвером формату.
        :param Weather weather: Информация о погоде, полученная от погодного провайдера.
        """
        res: OrderedDict = weather.get()

        for key in self.__format:
            # для каждого указанного ключа - перемещаем его на верх словаря
            res.move_to_end(key, False)

        return Weather(res)

    def save(self, weather: Weather, file_name: str):
        """
        Сохранение в файл информации о погоде в требуемом формате.
        :param Weather weather: Информация о погоде, полученная от погодного провайдера.
        :param str file_name: Путь сохранения файла.
        """
        formated_weather = self._format_weather(weather)

        with open(file_name, "w") as out:
            # контейнер с погодой изначально хранит всю информацию в JSON формате
            out.write(str(formated_weather))
