print ('Задание № 4')

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for string in name_list:
    right_name = string.split()[-1].capitalize()
    print(f"Привет, {right_name}!")
