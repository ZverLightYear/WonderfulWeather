from core.provider_manager import WeatherProviderManager
from core.saver_manager import WeatherSaverManager


class WeatherToFile:
    """
    Класс, для запроса погоды и сохранения в файл по заданным параметрам.
    """
    def __init__(self, config):
        """
        Инициализация экземпляра класса конфигурационным файлом.
        :param dict config: конфигурационный файл.
        """
        self._providers_init = config["providers"]
        self._savers_init = config["savers"]

        self._provider_types = list(self._providers_init.keys())
        self._saver_types = list(self._savers_init.keys())

    def get_weather_for_city_and_save(self, provider_type, saver_type, city, out_file_name):
        """
        Запрос погоды и сохранение ее в файл.
        :param str provider_type: Какой провайдер использовать для получения погоды?
        :param str saver_type: Какой сэйвер использовать для получения погоды?
        :param str city: Для какого города запросить погоду?
        :param str out_file_name: Куда сохранить результаты запроса?
        """
        # Тестовый прогон запроса погоды по параметрам
        provider_manager = WeatherProviderManager(self._providers_init)
        saver = WeatherSaverManager(self._savers_init)

        weather = provider_manager.get_weather_for_city(provider_type, city)
        if weather:
            print(weather)
            saver.save(weather, out_file_name, saver_type)
