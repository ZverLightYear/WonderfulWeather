# WonderfulWeather
```
usage: ww.py [-h] [-p {OpenWeatherMap,WeatherStack}] [-f {json,xml}] [-o O] city
positional arguments:
  city                  Город, для которого необходимо получить погоду.

optional arguments:
  -h, --help            show this help message and exit
  -p {OpenWeatherMap,WeatherStack}
                        Provider: Выбор погодного провайдера.
  -f {json,xml}         Format: Выбор типа сохраняемого файла.
  -o O                  Output: Поместить результат в выходной файл. По
                        умолчанию результаты сохраняются в ./output
```

Реализация на Python3.7
## Requirements:
  * requests >= 2.24.0
  * json2xml >= 3.4.1


## Пример конфигурационного файла conf.json:
```
{
  "providers": {
    "OpenWeatherMap": {
      "url": "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric",
      "api_key": "6d28a5b2f17fbc0521aa16d2d20e59f3"
    },
    "WeatherStack": {
      "url": "http://api.weatherstack.com/current?query={}&access_key={}&units=m",
      "api_key": "83d9a2d5ba08bf84a54962289dc40033"
    }
  },
  "savers": {
    "json": {
      "json_order": ["date", "temp", "wind_deg"]
    },
    "xml": {
      "xml_order":["date", "wind_speed", "temp"]
    }
  }
}
```
`providers` - содержит информацию о реализованных погодных провайдерах (API)
  Для каждого реализованного провайдера задается набор параметров, необходимых для корректной работы. Набор параметров для каждой реализации может быть произвольным.
  Для реализованных (`OpenWeatherMap`, `WeatherStack`) провайдеров указывается `url` запроса (как правило - не меняется), а также `api_key` - уникальный ключ, который выдается на аккаунт (необходима регистрация на сервисе). В данных реализациях указан ключ с моего тестового аккаунта.
  
`savers` - содержит информацию о реализованных погодных сэйверах
  Для каждого реализованного сэйвера задается набор параметров, необходимых для корректной работы. Набор параметров для каждой реализации может быть произвольным.
  Для реализованных (`xml`, `json`) сэйверов указывается поля (и их порядок), которые будут сохранены в файле.
  Набор доступных полей:
    `date` - дата, для которой актуальны показатели температуры
    `temp` - температура воздуха
    `feels_like` - ощущаемая температура воздуха
    `pressure` - давление,
    `humidity` - влажность,
    `visibility` - видимость,
    `cloudcover` - облачность,
    `location_name` - город, для которого запрашивалась температура,
    `location_lon`, `location_lat` - координаты города в сферической системе координат,
    `wind_speed` - сила ветра,
    `wind_deg` - направление ветра  
 
