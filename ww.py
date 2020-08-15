import json
import datetime

from core.provider_manager import WeatherProviderManager
from core.saver_manager import WeatherSaverManager


if __name__ == '__main__':
    # Подгружаем конфигурационный файл
    config = json.load(open("conf.json", "r"))

    # В конфигурационном файле содержится информация для инициализации погодных провайдеров и сэйверов
    providers_init = config["providers"]
    savers_init = config["savers"]

    # ToDo: parse args:
    # [-p provider] [-k appid]? city [-f format_to_save]
    city = "Moscow"
    # provider_type = "OpenWeatherMap"
    # saver_type = "xml"
    provider_types = ["OpenWeatherMap", "WeatherStack"]
    saver_types = ["xml", "json"]

    # Тестовый прогон запроса погоды для всех провайдеров и типов данных
    provider_manager = WeatherProviderManager(providers_init)
    saver = WeatherSaverManager(savers_init)

    now = datetime.datetime.now()
    for provider_type in provider_types:
        for saver_type in saver_types:
            # генерируем имя выходного файла для сохранения
            out_file_name = f'{city}_{provider_type}_{now.strftime("%d-%m-%Y_%H-%M-%S")}.{saver_type}'

            weather = provider_manager.get_weather_for_city(provider_type, city)
            saver.save(weather, f"output/{out_file_name}", saver_type)
