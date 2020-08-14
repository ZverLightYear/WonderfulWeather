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

    def __str__(self):
        """
        :return: Читабельное представление погоды.
        """
        return json.dumps(self.__weather, indent=4)

    def get(self):
        """
        :return: Представление погоды.
        """
        return copy(self.__weather)
