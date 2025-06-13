# Дни недели для формулы Зеллера
RU_DAYS = {
    "2": "Понедельник",
    "3": "Вторник",
    "4": "Среда",
    "5": "Четверг",
    "6": "Пятница",
    "0": "Суббота",
    "1": "Воскресенье"
}


RU_MONTHS = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }


RU_WIND_DIR = {
    "N": "С", "NNE": "ССВ", "NE": "СВ", "ENE": "ВСВ",
    "E": "В", "ESE": "ВЮВ", "SE": "ЮВ", "SSE": "ЮЮВ",
    "S": "Ю", "SSW": "ЮЮЗ", "SW": "ЮЗ", "WSW": "ЗЮЗ",
    "W": "З", "WNW": "ЗСЗ", "NW": "СЗ", "NNW": "ССЗ"
}


# Самое сложное сделал ИИ - сопоставил коды
# состояний погоды сервиса и плеера Коди
# Не реклама, констатация факта -
# ChatGPT и chat.qwen.ai облажались!!!
# справился с этим только chat.deepseek.com
# со всеми правками ушло минут 20, полчаса макс.

ICONS_AND_RU_CONDITIONS = {
    # Ясная погода
    1000: {  # Sunny
        "day": {"icon": "32.png", "text_ru": "Солнечно"},
        "night": {"icon": "31.png", "text_ru": "Ясно"}
    },

    # Облачность
    1003: {  # Partly cloudy
        "day": {"icon": "28.png", "text_ru": "Переменная облачность"},
        "night": {"icon": "27.png", "text_ru": "Переменная облачность"}
    },
    1006: {  # Cloudy
        "day": {"icon": "26.png", "text_ru": "Облачно"},
        "night": {"icon": "26.png", "text_ru": "Облачно"}
    },
    1009: {  # Overcast
        "day": {"icon": "26.png", "text_ru": "Пасмурно"},
        "night": {"icon": "26.png", "text_ru": "Пасмурно"}
    },
    1030: {  # Mist
        "day": {"icon": "21.png", "text_ru": "Дымка"},
        "night": {"icon": "21.png", "text_ru": "Дымка"}
    },
    1135: {  # Fog
        "day": {"icon": "20.png", "text_ru": "Туман"},
        "night": {"icon": "20.png", "text_ru": "Туман"}
    },
    1147: {  # Freezing fog
        "day": {"icon": "20.png", "text_ru": "Ледяной туман"},
        "night": {"icon": "20.png", "text_ru": "Ледяной туман"}
    },

    # Дождь
    1063: {  # Patchy rain possible
        "day": {"icon": "11.png", "text_ru": "Возможен дождь"},
        "night": {"icon": "45.png", "text_ru": "Возможен дождь"}
    },
    1072: {  # Patchy freezing drizzle possible
        "day": {"icon": "8.png", "text_ru": "Возможен ледяной дождь"},
        "night": {"icon": "8.png", "text_ru": "Возможен ледяной дождь"}
    },
    1150: {  # Patchy light drizzle
        "day": {"icon": "9.png", "text_ru": "Морось"},
        "night": {"icon": "9.png", "text_ru": "Морось"}
    },
    1153: {  # Light drizzle
        "day": {"icon": "9.png", "text_ru": "Слабая морось"},
        "night": {"icon": "9.png", "text_ru": "Слабая морось"}
    },
    1168: {  # Freezing drizzle
        "day": {"icon": "8.png", "text_ru": "Ледяная морось"},
        "night": {"icon": "8.png", "text_ru": "Ледяная морось"}
    },
    1171: {  # Heavy freezing drizzle
        "day": {"icon": "8.png", "text_ru": "Сильная ледяная морось"},
        "night": {"icon": "8.png", "text_ru": "Сильная ледяная морось"}
    },
    1180: {  # Patchy light rain
        "day": {"icon": "11.png", "text_ru": "Местами слабый дождь"},
        "night": {"icon": "45.png", "text_ru": "Местами слабый дождь"}
    },
    1183: {  # Light rain
        "day": {"icon": "11.png", "text_ru": "Небольшой дождь"},
        "night": {"icon": "45.png", "text_ru": "Небольшой дождь"}
    },
    1186: {  # Moderate rain at times
        "day": {"icon": "11.png", "text_ru": "Временами умеренный дождь"},
        "night": {"icon": "45.png", "text_ru": "Временами умеренный дождь"}
    },
    1189: {  # Moderate rain
        "day": {"icon": "11.png", "text_ru": "Умеренный дождь"},
        "night": {"icon": "45.png", "text_ru": "Умеренный дождь"}
    },
    1192: {  # Heavy rain at times
        "day": {"icon": "12.png", "text_ru": "Временами сильный дождь"},
        "night": {"icon": "12.png", "text_ru": "Временами сильный дождь"}
    },
    1195: {  # Heavy rain
        "day": {"icon": "12.png", "text_ru": "Сильный дождь"},
        "night": {"icon": "12.png", "text_ru": "Сильный дождь"}
    },
    1198: {  # Light freezing rain
        "day": {"icon": "10.png", "text_ru": "Слабый ледяной дождь"},
        "night": {"icon": "10.png", "text_ru": "Слабый ледяной дождь"}
    },
    1201: {  # Moderate or heavy freezing rain
        "day": {"icon": "10.png", "text_ru": "Ледяной дождь"},
        "night": {"icon": "10.png", "text_ru": "Ледяной дождь"}
    },
    1240: {  # Light rain shower
        "day": {"icon": "11.png", "text_ru": "Небольшой ливень"},
        "night": {"icon": "45.png", "text_ru": "Небольшой ливень"}
    },
    1243: {  # Moderate or heavy rain shower
        "day": {"icon": "12.png", "text_ru": "Ливень"},
        "night": {"icon": "12.png", "text_ru": "Ливень"}
    },
    1246: {  # Torrential rain shower
        "day": {"icon": "12.png", "text_ru": "Проливной ливень"},
        "night": {"icon": "12.png", "text_ru": "Проливной ливень"}
    },

    # Снег
    1066: {  # Patchy snow possible
        "day": {"icon": "13.png", "text_ru": "Возможен снег"},
        "night": {"icon": "13.png", "text_ru": "Возможен снег"}
    },
    1114: {  # Blowing snow
        "day": {"icon": "15.png", "text_ru": "Метель"},
        "night": {"icon": "15.png", "text_ru": "Метель"}
    },
    1117: {  # Blizzard
        "day": {"icon": "15.png", "text_ru": "Снежная буря"},
        "night": {"icon": "15.png", "text_ru": "Снежная буря"}
    },
    1204: {  # Light sleet
        "day": {"icon": "18.png", "text_ru": "Слабый мокрый снег"},
        "night": {"icon": "18.png", "text_ru": "Слабый мокрый снег"}
    },
    1207: {  # Moderate or heavy sleet
        "day": {"icon": "18.png", "text_ru": "Мокрый снег"},
        "night": {"icon": "18.png", "text_ru": "Мокрый снег"}
    },
    1210: {  # Patchy light snow
        "day": {"icon": "14.png", "text_ru": "Местами слабый снег"},
        "night": {"icon": "14.png", "text_ru": "Местами слабый снег"}
    },
    1213: {  # Light snow
        "day": {"icon": "14.png", "text_ru": "Небольшой снег"},
        "night": {"icon": "14.png", "text_ru": "Небольшой снег"}
    },
    1216: {  # Patchy moderate snow
        "day": {"icon": "16.png", "text_ru": "Местами умеренный снег"},
        "night": {"icon": "16.png", "text_ru": "Местами умеренный снег"}
    },
    1219: {  # Moderate snow
        "day": {"icon": "16.png", "text_ru": "Умеренный снег"},
        "night": {"icon": "16.png", "text_ru": "Умеренный снег"}
    },
    1222: {  # Patchy heavy snow
        "day": {"icon": "41.png", "text_ru": "Местами сильный снег"},
        "night": {"icon": "41.png", "text_ru": "Местами сильный снег"}
    },
    1225: {  # Heavy snow
        "day": {"icon": "41.png", "text_ru": "Сильный снег"},
        "night": {"icon": "41.png", "text_ru": "Сильный снег"}
    },
    1237: {  # Ice pellets
        "day": {"icon": "17.png", "text_ru": "Ледяная крупа"},
        "night": {"icon": "17.png", "text_ru": "Ледяная крупа"}
    },
    1249: {  # Light sleet showers
        "day": {"icon": "18.png", "text_ru": "Слабый мокрый снег"},
        "night": {"icon": "18.png", "text_ru": "Слабый мокрый снег"}
    },
    1252: {  # Moderate or heavy sleet showers
        "day": {"icon": "18.png", "text_ru": "Мокрый снег"},
        "night": {"icon": "18.png", "text_ru": "Мокрый снег"}
    },
    1255: {  # Light snow showers
        "day": {"icon": "14.png", "text_ru": "Снежные заряды"},
        "night": {"icon": "14.png", "text_ru": "Снежные заряды"}
    },
    1258: {  # Moderate or heavy snow showers
        "day": {"icon": "16.png", "text_ru": "Снегопад"},
        "night": {"icon": "16.png", "text_ru": "Снегопад"}
    },
    1261: {  # Light showers of ice pellets
        "day": {"icon": "17.png", "text_ru": "Ледяная крупа"},
        "night": {"icon": "17.png", "text_ru": "Ледяная крупа"}
    },
    1264: {  # Moderate or heavy showers of ice pellets
        "day": {"icon": "17.png", "text_ru": "Сильная ледяная крупа"},
        "night": {"icon": "17.png", "text_ru": "Сильная ледяная крупа"}
    },

    # Гроза
    1087: {  # Thundery outbreaks possible
        "day": {"icon": "37.png", "text_ru": "Возможна гроза"},
        "night": {"icon": "37.png", "text_ru": "Возможна гроза"}
    },
    1273: {  # Patchy light rain with thunder
        "day": {"icon": "37.png", "text_ru": "Гроза со слабым дождем"},
        "night": {"icon": "37.png", "text_ru": "Гроза со слабым дождем"}
    },
    1276: {  # Moderate or heavy rain with thunder
        "day": {"icon": "4.png", "text_ru": "Гроза с дождем"},
        "night": {"icon": "4.png", "text_ru": "Гроза с дождем"}
    },
    1279: {  # Patchy light snow with thunder
        "day": {"icon": "37.png", "text_ru": "Гроза со слабым снегом"},
        "night": {"icon": "37.png", "text_ru": "Гроза со слабым снегом"}
    },
    1282: {  # Moderate or heavy snow with thunder
        "day": {"icon": "4.png", "text_ru": "Гроза со снегом"},
        "night": {"icon": "4.png", "text_ru": "Гроза со снегом"}
    },

    # Экстремальные явления
    1118: {  # Freezing fog
        "day": {"icon": "20.png", "text_ru": "Ледяной туман"},
        "night": {"icon": "20.png", "text_ru": "Ледяной туман"}
    },
    1285: {  # Blizzard
        "day": {"icon": "15.png", "text_ru": "Метель"},
        "night": {"icon": "15.png", "text_ru": "Метель"}
    },

    # Пыль/песок
    1271: {  # Duststorm
        "day": {"icon": "19.png", "text_ru": "Пыльная буря"},
        "night": {"icon": "19.png", "text_ru": "Пыльная буря"}
    },
    1274: {  # Sandstorm
        "day": {"icon": "19.png", "text_ru": "Песчаная буря"},
        "night": {"icon": "19.png", "text_ru": "Песчаная буря"}
    }
}

