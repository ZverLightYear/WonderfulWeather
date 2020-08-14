import json
import datetime

from core.weather_provider import WeatherProvider
from core.weather_providers.OpenWeatherMap import OpenWeatherMap
from core.weather_providers.WeatherStack import WeatherStack

from core.weather_saver import WeatherSaver
from core.weather_savers.json_saver import JsonWeatherSaver
from core.weather_savers.xml_saver import XmlWeatherSaver


if __name__ == '__main__':
    # Подгружаем конфигурационный файл
    config = json.load(open("conf.json", "r"))

    # В конфигурационном файле содержится информация для инициализации погодных провайдеров
    providers_init = config["providers"]
    savers_init = config["savers"]

    # ToDo: parse args:
    # [-p provider] [-k appid]? city [-f format_to_save]

    city = "Moscow"

    # Тестовый прогон запроса погоды через API OpenWeatherMap
    # Создаем и инициализируем провайдер OpenWeatherMap
    provider: WeatherProvider = OpenWeatherMap(providers_init["OpenWeatherMap"])

    # Запрашиваем информацию о погоде в Москве
    weather = provider.get_weather_for_city(city)

    # генерируем имя выходного файла для сохранения
    now = datetime.datetime.now()
    out_file_name = f'{city}_{now.strftime("%d-%m-%Y_%H-%M-%S")}'

    # Тестовый прогон сохранения погоды через оба сейвера(JSON & XML)
    # Создаем и инициализируем сэйвер JsonWeatherSaver
    saver: WeatherSaver = JsonWeatherSaver(savers_init["json_format"])
    # Сохраняем результат
    saver.save(weather, f"output/{out_file_name}.json")

    # Создаем и инициализируем сэйвер XmlWeatherSaver
    saver: WeatherSaver = XmlWeatherSaver(savers_init["xml_format"])
    # Сохраняем результат
    saver.save(weather, f"output/{out_file_name}.xml")

    # Тестовый прогон запроса погоды через API WeatherStack
    provider: WeatherProvider = WeatherStack(providers_init["WeatherStack"])
    # Запрашиваем информацию о погоде в Москве
    weather = provider.get_weather_for_city(city)

    print(weather)

