from json2xml.json2xml import Json2xml

from core.weather import Weather
from core.weather_saver import WeatherSaver


class XmlWeatherSaver(WeatherSaver):
    """
    Реализация сэйвера данных о погоде в формате XML.
    """

    def save(self, weather: Weather, file_name: str):
        # ToDo: порядок сохранения полей
        with open(file_name, "w") as out:
            # Перед записью преобразуем данные из JSON в XML
            out.write(Json2xml(weather.get()).to_xml())
