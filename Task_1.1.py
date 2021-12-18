# Домашнее задание к уроку 1 "Знакомство с Python"
# Задание № 1
print('Задание №1')

one_minute = 60  # 1 минута = 60 секунд
one_hour = 3600  # 1 час = 60*60 = 3600 секунд
one_day = 86400  # 1 сутки = 60*60*24 = 86400 секунд

duration = int(input('Введите время в секундах: '))

if duration < one_minute:
    print('{} сек'.format(duration))  # вывод времени в секундах

elif one_minute <= duration < one_hour:
    new_minute = duration // one_minute
    new_second = duration % one_minute
    print('{} мин. {} сек.'.format(new_minute, new_second))  # вывод времени в минутах и секундах

elif one_hour <= duration < one_day:
    new_hour = duration // one_hour
    duration = duration % one_hour
    new_minute = duration // one_minute
    new_second = duration % one_minute
    print('{} ч. {} мин. {} сек.'.format(new_hour, new_minute, new_second))  # вывод времени в часах, минутах, секундах

elif duration >= one_day and duration > one_day:
    new_day = duration // one_day
    duration = duration % one_day
    new_hour = duration // one_hour
    duration = duration % one_hour
    new_minute = duration // one_minute
    new_second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(new_day, new_hour, new_minute,
                                              new_second))  # вывод времени в днях, часах, минутах, секундах
