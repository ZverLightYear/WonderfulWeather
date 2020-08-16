import json
from collections import OrderedDict

from copy import copy


class Weather:
    """
    Контейнер для хранения ответов от погодных провайдеров.
    Предполагается изначальное хранение погоды в OrderedDict (JSON) формате.
    """

    __weather: OrderedDict = None

    def __init__(self, weather: OrderedDict):
        """
        :param OrderedDict weather: Показатели погоды.
        """
        self.__weather = weather

    @staticmethod
    def _wind_vector_symbol(wind_deg):
        """
        Представление направления ветра в символьном виде
        :param int wind_deg: направление ветра в градусах.
        :return tuple: Направление ветра (буквенное_представление, символьное_представление).
        """
        wind_vector = {
            ("ЮЗ", "🡭"): lambda x: 22.5 < x <= 67.5,
            ("Ю",  "🡩"): lambda x: 67.5 < x <= 112.5,
            ("ЮВ", "🡬"): lambda x: 112.5 < x <= 157.5,
            ("В",  "🡨"): lambda x: 157.5 < x <= 202.5,
            ("СВ", "🡯"): lambda x: 202.5 < x <= 247.5,
            ("С",  "🡫"): lambda x: 247.5 < x <= 292.5,
            ("СЗ", "🡮"): lambda x: 292.5 < x <= 337.5,
            ("З",  "🡪"): lambda x: x <= 22.5 or x > 337.5
        }

        for key in wind_vector:
            if wind_vector[key](wind_deg):
                return key[1]

    def __str__(self):
        """
        :return: Читабельное представление погоды.
        """
        out = f"Погода в '{self.__weather['location_name']}':" \
              f"\n\t{self.__weather['temp']}°C" \
              f"\n\t{self.__weather['wind_speed']} m/s {self._wind_vector_symbol(self.__weather['wind_speed'])}" \
              f"\n\tВлажность: {self.__weather['humidity']}%"
        return out

    def __getitem__(self, key):
        return self.__weather[key]

    def json(self):
        return json.dumps(self.__weather, indent=4)

    def get(self):
        """
        :return Weather: Контейнер погоды.
        """
        return copy(self.__weather)
