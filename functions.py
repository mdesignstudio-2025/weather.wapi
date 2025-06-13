import requests
import xbmcgui
import xbmcaddon
from consts import (
    RU_DAYS,
    RU_MONTHS,
    RU_WIND_DIR,
    ICONS_AND_RU_CONDITIONS
)


window = xbmcgui.Window(12600)
ADDON = xbmcaddon.Addon()



def set_weather (current: dict, daily: list, hourly: list, args: str):

    # Заполняем шапку
    location_value = window.getProperty(f"Location{args}")
    window.setProperty("Current.Location", location_value)
    window.setProperty("WeatherProvider", "WeatherAPI.com")
    window.setProperty("Current.Temperature", f"{round(current['temp_c'])}°C")
    window.setProperty("Current.FeelsLike", f"{round(current['feelslike_c'])}°C")
    window.setProperty("Current.Condition", current['condition']['text'])

    # В шапке этого значка не будет, но он появится под часами, если включить опцию
    # "Интерфейс - Настройки обложки - Показать сведения о погоде на верхней панели"
    window.setProperty("Current.OutlookIcon", current['condition']['code'])

    window.setProperty("Current.WindDirection", current['wind_dir'])
    window.setProperty("Current.Wind", f"{str(current['wind_kph'])}")

    window.setProperty("Current.Humidity", f"Влажность\n{current['humidity']}")
    window.setProperty("Current.Precipitation", f"Осадки\n{current['precip_mm']} мм")

    # Загадка для меня, но восход и закат заполняются ТОЛЬКО с Today!
    # если указать Current - НЕ ПОЯВЛЯЮТСЯ!!!
    window.setProperty("Today.Sunrise", f"Восход\n{current['vosxod']}")
    window.setProperty("Today.Sunset", f"Закат\n{current['zakat']}")

    #Объявляем эту часть погоды (current) заполненной и готовой к показу
    window.setProperty("Current.IsFetched", "true")


    # В цикле заполняем плашки первого(верхнего) ряда - погода на 14 дней
    for i, day in enumerate(daily):

        # !!! ВАЖНО !!!
        # Питоновские циклы начинаются с 0, а элементы коди нумеруются с 1!
        # В значении часа добавляем 1 (i+1), иначе первое значение (день/час) из цикла НЕ ОТОБРАЖАЕТСЯ!
        window.setProperty(f"Daily.{i+1}.ShortDate", day['date'])
        window.setProperty(f"Daily.{i+1}.ShortDay", day['day_of_week'])
        window.setProperty(f"Daily.{i+1}.LowTemperature", f"{round(day['mintemp_c'])}°C")
        window.setProperty(f"Daily.{i+1}.HighTemperature", f"{round(day['maxtemp_c'])}°C")
        window.setProperty(f"Daily.{i+1}.OutlookIcon", day['condition']['code'])

        # !!!!! ВАЖНО !!!!!
        # Хотя в скине Estuary значения Outlook не отображаются, НО
        # без заполнения Outlook плашки СОЗДАВАТЬСЯ НЕ БУДУТ!!!
        window.setProperty(f"Daily.{i+1}.Outlook", f"{day['condition']['text']}")

    # Объявляем эту часть погоды (daily) заполненной и готовой к показу
    window.setProperty("Daily.IsFetched", "true")


    # В цикле заполняем плашки второго(нижнего) ряда - погода на 24 часа
    for i, hour in enumerate(hourly):

        # !!! ВАЖНО !!!
        # Питоновские циклы начинаются с 0, а элементы коди нумеруются с 1!
        # Поэтому в значении часа добавляем 1 (i+1)
        window.setProperty(f"Hourly.{i+1}.Time", f"{hour['time']}")
        window.setProperty(f"Hourly.{i+1}.ShortDate", f"{hour['date']}")
        window.setProperty(f"Hourly.{i+1}.Temperature", f"{round(hour['temp_c'])}°C")
        window.setProperty(f"Hourly.{i+1}.Precipitation", f"{hour['precip_mm']} мм")
        window.setProperty(f"Hourly.{i+1}.OutlookIcon", hour['condition']['code'])

        # !!!!! ВАЖНО !!!!!
        # Хотя в скине Estuary значения Outlook не отображаются, НО
        # без заполнения Outlook плашки СОЗДАВАТЬСЯ НЕ БУДУТ!!!
        window.setProperty(f"Hourly.{i+1}.Outlook", hour['condition']['text'])

    # Объявляем эту часть погоды (hourly) заполненной и готовой к показу
    window.setProperty("Hourly.IsFetched", "true")



def update_condition(data):
    # Если это один элемент (не список), оборачиваем его в список
    if not isinstance(data, list):
        data = [data]

    for item in data:
        condition = item.get("condition", {})
        condition_code = condition.get("code")

        is_day = item.get("is_day", 1)  # По умолчанию день

        if condition_code is not None:
            weather_data = ICONS_AND_RU_CONDITIONS.get(condition_code, {
                "day": {"icon": "na.png", "text_ru": "Неизвестно"},
                "night": {"icon": "na.png", "text_ru": "Неизвестно"}
            })

            time_of_day = "day" if is_day == 1 else "night"
            icon = weather_data[time_of_day]["icon"]
            text_ru = weather_data[time_of_day]["text_ru"]

            item["condition"] = {
                "text": text_ru,
                "code": icon
            }



def parse_weather(data: dict):

    # 1. current_w
    current = data["current"]
    wind_dir_ru = RU_WIND_DIR.get(current["wind_dir"], current["wind_dir"])
    astro = data["forecast"]["forecastday"][0]["astro"]
    vosxod = convert_time(astro.get("sunrise"))
    zakat = convert_time(astro.get("sunset"))

    current_w = {
        "temp_c": current["temp_c"],
        "is_day": current["is_day"],
        "condition": current["condition"],
        "wind_kph": current["wind_kph"],
        "wind_dir": wind_dir_ru,
        "precip_mm": current["precip_mm"],
        "humidity": current["humidity"],
        "feelslike_c": current["feelslike_c"],
        "vosxod": vosxod,
        "zakat": zakat
    }

    update_condition(current_w)

    # 2. daily_w
    daily_w = []

    for forecast_day in data["forecast"]["forecastday"]:
        # Получаем день недели
        day_of_week = get_day_of_week(forecast_day["date"])
        ru_date = ru_format_date(forecast_day["date"])
        # Формируем запись
        day_data = {
            "date": ru_date,
            "day_of_week": day_of_week,  # Добавляем день недели
            **forecast_day["day"]  # Остальные поля (maxtemp_c, mintemp_c...)
        }
        daily_w.append(day_data)

    update_condition(daily_w)


    # 3. hourly_w
    hourly_w = []

    for day in data['forecast']['forecastday']:
        for hour in day['hour']:
            # Разделяем 'time' (формат: '2025-05-02 22:00')
            full_time = hour.pop('time')  # Удаляем 'time' и забираем значение
            date, time = full_time.split(' ')  # Разделяем дату и время
            ru_date = ru_format_date(date)
            ru_time = f"{int(time.split(':')[0])}:{time.split(':')[1]}"
            # Формируем новый словарь с правильной структурой
            hour_data = {
                'date': ru_date,  # '2025-05-02' (взято из time)
                'time': ru_time,
                **hour  # Остальные поля (temp_c, condition и т.д.)
            }

            hourly_w.append(hour_data)

    update_condition(hourly_w)

    return current_w, daily_w, hourly_w



def get_weather(api_key, location, days):
    """Получить данные о погоде с WeatherAPI.com"""
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"
    response = requests.get(url)
    data = response.json()
    filter_future_hours_only(data)
    return data



def ru_format_date(date_str):
    year, month, day = map(int, date_str.split('-'))

    return f"{day} {RU_MONTHS[month]}"



def get_day_of_week(date_str):
    # Используем формулу Зеллера для получения дня недели из даты
    year, month, day = map(int, date_str.split('-'))

    if month < 3:
        month += 12
        year -= 1

    q = day         # День месяца
    m = month       # Месяц (от 3 до 14)
    K = year % 100  # Последние две цифры года
    J = year // 100 # Первые две цифры года

    h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    # Возвращаем 0 = Saturday, 1 = Sunday, ..., 6 = Friday

    return RU_DAYS[str(h)]


def convert_time(time_str):
    """
    Конвертирует время из формата 'hh:mm AM/PM' в 24-часовой формат 'H:mm'.
    Возвращает часы без ведущего нуля, но минуты — всегда с нулём.

    :param time_str: Время в формате 'hh:mm AM/PM' (например, '06:21 AM').
    :return: Время в 24-часовом формате (например, '6:21').
    """
    time_part, am_pm = time_str.split()
    hours, minutes = map(int, time_part.split(':'))

    if am_pm.upper() == "PM" and hours != 12:
        hours += 12
    elif am_pm.upper() == "AM" and hours == 12:
        hours = 0

    return f"{hours}:{minutes:02d}"  # Часы как есть, минуты с нулём


# Функция для показа только тех часов погоды, которые больше текущего времени
def filter_future_hours_only(weather_data):
    current_time_str = weather_data["location"]["localtime"]

    for day in weather_data["forecast"]["forecastday"]:
        if "hour" in day:
            # Оставляем только те часы, которые > current_time_str
            day["hour"] = [h for h in day["hour"] if h["time"] > current_time_str]


def determine_location ():

    # Получаем все заполненные локации из settings.xml
    locs_wapi = []
    for i in range(1, 4):
        loc_value = ADDON.getSetting(f'loc{i}_wapi')  # Получаем значение
        if loc_value and loc_value.strip():  # Проверяем не пустое ли значение
            locs_wapi.append(loc_value.strip())  # Добавляем без пробелов по краям

    # Сообщаем Коди сколько всего локаций ввел пользователь
    # количество локаций вводится как СТРОКА, НЕ как число!!!
    window.setProperty("Locations", str(len(locs_wapi)))

    # Заполняем Location№ введенными пользователем названиями для отображения в погоде
    for i in range(1, 4):
        # Получаем оба значения
        wapi_name = ADDON.getSetting('loc{}_wapi'.format(i)).strip()  # Для парсера (eng)
        user_name = ADDON.getSetting('loc{}_user'.format(i)).strip()  # Для отображения

        # Выбираем имя для отображения (пользовательское или парсера)
        display_name = user_name if user_name else wapi_name.capitalize()

        # Устанавливаем свойство
        if display_name:  # Если хотя бы одно имя есть
            window.setProperty("Location{}".format(i), display_name)

# Использовалась при отладке для вывода сообщений
def gui_message (title, message):
    dialog = xbmcgui.Dialog()
    dialog.ok(title, message)
