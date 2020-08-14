import json


class Weather:
    """
    Контейнер для хранения ответов от погодных провайдеров.
    """

    __weather = None

    def __init__(self, weather: dict):
        """
        :param dict weather: Показатели погоды
        """
        self.__weather = weather

    def __repr__(self):
        """
        :return: Читабельное представление погоды
        """
        return json.dumps(self.__weather, indent=4)
