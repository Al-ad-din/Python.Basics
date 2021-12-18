print('Задание №2')

a = [x ** 3 for x in range(1000) if x % 2 != 0]
print('Cписок № 1: список кубов нечётных чисел {}'.format(a))

b = []
sum_1 = 0
for num in a:
    i = num
    while num != 0:
        sum_1 += num % 10
        num = num // 10
    if sum_1 % 7 == 0:
        b.append(i)
    sum_1 = 0
print('Cумма чисел из списка № 1, сумма цифр которых делится нацело на 7: ', sum(b))

sum_new = 0
for num in a:
    suma = 0
    i = num
    num += 17
    while num != 0:
        suma += num % 10
        num = num // 10
    if suma % 7 == 0:
        sum_new += i

print('Cумма чисел из списка № 1, увеличенных на 17, сумма цифр которых делится нацело на 7: ', sum_new)
