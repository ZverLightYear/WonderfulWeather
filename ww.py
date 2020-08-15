import argparse

import json
import datetime

from core.provider_manager import WeatherProviderManager
from core.saver_manager import WeatherSaverManager


def parse_args():
    parser = argparse.ArgumentParser(description='Брать ли с собой зонтик в дорогу?')
    parser.add_argument("-p",
                        default=provider_types[0],
                        choices=provider_types,
                        help="Provider: Выбор погодного провайдера.")
    parser.add_argument("-f",
                        default=saver_types[0],
                        choices=saver_types,
                        help="Format: Выбор типа сохраняемого файла.")
    parser.add_argument("-o",
                        help="Output: Поместить результат в выходной файл.\n"
                             "По умолчанию результаты сохраняются в {./output}.")
    parser.add_argument("city",
                        help="Город, для которого необходимо получить погоду.")
    return parser.parse_args()


if __name__ == '__main__':
    # Подгружаем конфигурационный файл
    # В конфигурационном файле содержится информация для инициализации погодных провайдеров и сэйверов
    config = json.load(open("conf.json", "r"))
    providers_init = config["providers"]
    savers_init = config["savers"]

    provider_types = list(providers_init.keys())
    saver_types = list(savers_init.keys())

    # Парсим и извлекаем аргументы
    args = parse_args()
    provider_type, saver_type, city = args.p, args.f, args.city

    # генерируем имя выходного файла для сохранения
    now = datetime.datetime.now()
    out_file_name = f'output/{city}_{provider_type}_{now.strftime("%d-%m-%Y_%H-%M-%S")}.{saver_type}'
    if args.o:
        out_file_name = args.o

    # Тестовый прогон запроса погоды по параметрам
    provider_manager = WeatherProviderManager(providers_init)
    saver = WeatherSaverManager(savers_init)

    weather = provider_manager.get_weather_for_city(provider_type, city)
    saver.save(weather, out_file_name, saver_type)
