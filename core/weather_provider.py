from __future__ import annotations
from abc import abstractmethod, ABC

from core.weather import *


class WeatherProvider(ABC):
    """
    Интерфейс погодного провайдера.
    Объявляет операции, которые должны выполнять все реализации погодных провайдеров.
    """

    @abstractmethod
    def __init__(self):
        """
        Инициализация провайдера для корректной работы.
        """
        pass

    @abstractmethod
    def get_weather_for_city(self, city) -> Weather:
        """
        Метод получания данных о погоде для заданного города.
        :param str city: Город, для которого запрашивается погода.
        """
        pass


