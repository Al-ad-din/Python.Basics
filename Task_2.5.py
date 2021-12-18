print('Задание № 5')

import random

price_list = [round(random.uniform(1, 100), 2) for i in range(20)]
print('Прайс-лист: ', price_list)
print('Идентификатор прайс-листа: ', id(price_list))
price_list.sort()
print('Идентификатор прайс-листа после сортировки: ', id(price_list))

store_id = id(price_list)
print('Сортировка цен по возрастанию: ', price_list)

print('Вывод цен в рублях и копейках: ')

end_word: str = ", "

for i, num in enumerate(price_list):
    fix_price = str(f"{float(num):.2f}").split(".")
    if i == len(price_list) - 1:
        end_word = "\n"
    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)

print(f"Идентификатор прайс-листа перед сортировкой: {store_id}")
price_list.sort()
print('Сортировка цен по возрастанию: ', price_list)
print(f"Идентификатор прайс-листа после сортировки: {id(price_list)}")

if store_id == id(price_list):
    print("Идентификатор не изменился")
else:
    print("Идентификатор изменился")

copy_of_list = price_list.copy()  # or use input_list[:]
copy_of_list.sort(reverse=True)  # or use list(sorted()) without copy

print('Сортировка цен по убыванию: ', copy_of_list)
print('Идентификатор прайс-листа перед сортировкой:', store_id)
print('Идентификатор прайс-листа после сортировки:', id(copy_of_list))

if store_id == id(copy_of_list):
    print("Идентификатор не изменился")
else:
    print("Идентификатор изменился")

print("Список цен пяти дорогих товаров:", price_list[-6:-1])
