import json
from core.weather_provider import WeatherProvider
from core.weather_providers.OpenWeatherMap import OpenWeatherMap

if __name__ == '__main__':
    # Подгружаем конфигурационный файл
    config = json.load(open("conf.json", "r"))

    # В конфигурационном файле содержится информация для инициализации погодных провайдеров
    providers_init = config["providers"]

    # ToDo: parse args:
    # [-p provider] [-k appid]? location

    # Тестовый прогон запроса погоды через API OpenWeatherMap
    # Создаем и инициализируем провайдер OpenWeatherMap
    provider: WeatherProvider = OpenWeatherMap(providers_init["OpenWeatherMap"])

    # Запрашиваем информацию о погоде в Москве
    weather = provider.get_weather_for_city("Moscow")

    print(weather)
