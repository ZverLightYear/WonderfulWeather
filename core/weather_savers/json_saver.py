from core.weather import Weather
from core.weather_saver import WeatherSaver


class JsonWeatherSaver(WeatherSaver):
    """
    Реализация сэйвера данных о погоде в формате JSON.
    """

    def save(self, weather: Weather, file_name: str):
        # ToDo: порядок сохранения полей
        with open(file_name, "w") as out:
            # контейнер с погодой изначально хранит всю информацию в JSON формате
            out.write(str(weather))
