import json


class Weather:
    """
    Контейнер для хранения ответов от погодных провайдеров.
    Предполагается изначальное хранение погоды в JSON формате.
    """

    __weather: dict = None

    def __init__(self, weather: dict):
        """
        :param dict weather: Показатели погоды.
        """
        self.__weather = weather

    def __str__(self):
        """
        :return: Читабельное представление погоды
        """
        return json.dumps(self.__weather, indent=4)

    def __repr__(self):
        """
        :return: Представление погоды в формате JSON
        """
        return self.__weather
