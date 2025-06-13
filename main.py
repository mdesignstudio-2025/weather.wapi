import sys
import xbmcaddon
from functions import *

ADDON = xbmcaddon.Addon()
DAYS = ADDON.getSetting('days')
API_KEY = ADDON.getSetting('api_key')

def main():
    # Определяем сколько локаций, прописываем Location№
    determine_location()

    # Получаем строку с аргументами, переданными Коди нашему аддону
    # Игнорируем первый элемент (путь к скрипту) и
    # берем второй - номер локации (по умолчанию это ["1"])
    args = str(sys.argv[1])

    # Получаем из файла settings.xml значение локации
    # для парсера
    LOCATION = ADDON.getSetting(f'loc{args}_wapi')

    # Получаем данные от сервера
    weather_data = get_weather(API_KEY, LOCATION, DAYS)

    # Парсим полученные данные в форматы,
    # удобные для заполнения погодных плашек Коди
    current_pogoda, daily_pogoda, hourly_pogoda = parse_weather(weather_data)

    # Устанавливаем погоду в скин Коди
    set_weather (current_pogoda, daily_pogoda, hourly_pogoda, args)

if __name__ == "__main__":
    main()
