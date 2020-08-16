import argparse

import json
import datetime
import os

from core.weather_to_file import WeatherToFile


def parse_args():
    provider_types = list(config["providers"].keys())
    saver_types = list(config["savers"].keys())

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
                        help="Output: Поместить результат в выходной файл. "
                             "По умолчанию результаты сохраняются в ./output")
    parser.add_argument("city",
                        help="Город, для которого необходимо получить погоду.")
    return parser.parse_args()


if __name__ == '__main__':
    working_directory = os.path.dirname(__file__)

    # Подгружаем конфигурационный файл
    # В конфигурационном файле содержится информация для инициализации погодных провайдеров и сэйверов
    config = json.load(open(f"{working_directory}/conf.json", "r"))

    # Парсим и извлекаем аргументы
    args = parse_args()
    provider_type, saver_type, city = args.p, args.f, args.city
    # provider_type, saver_type, city = "WeatherStack", "xml", "Moscow"

    if args.o:
        out_file_name = args.o
    else:
        # генерируем имя выходного файла для сохранения
        out_dir = f'{working_directory}/output'
        now = datetime.datetime.now()
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)
        out_file_name = f'{out_dir}/{city}_{provider_type}_{now.strftime("%d-%m-%Y_%H-%M-%S")}.{saver_type}'

    # Запрашиваем погоду
    wtf: WeatherToFile = WeatherToFile(config)
    wtf.get_weather_for_city_and_save(provider_type, saver_type, city, out_file_name)
