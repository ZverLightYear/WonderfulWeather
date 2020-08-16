from __future__ import annotations
from abc import abstractmethod, ABC

from core.weather import *


class WeatherSaverInterface(ABC):
    """
    Интерфейс сэйвера погоды.
    Объявляет операции, которые должны выполнять все реализации погодных сейверов.
    """

    @abstractmethod
    def save(self, weather: Weather, file_name: str):
        """
        Метод сохранения данных о погоде.
        """
        pass


