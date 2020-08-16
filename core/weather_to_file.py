from core.provider_manager import WeatherProviderManager
from core.saver_manager import WeatherSaverManager


class WeatherToFile:
    def __init__(self, config):
        self._providers_init = config["providers"]
        self._savers_init = config["savers"]

        self._provider_types = list(self._providers_init.keys())
        self._saver_types = list(self._savers_init.keys())

    def request(self, provider_type, saver_type, city, out_file_name):
        # Тестовый прогон запроса погоды по параметрам
        provider_manager = WeatherProviderManager(self._providers_init)
        saver = WeatherSaverManager(self._savers_init)

        weather = provider_manager.get_weather_for_city(provider_type, city)
        if weather:
            print(weather)
            saver.save(weather, out_file_name, saver_type)
