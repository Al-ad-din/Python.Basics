print ('Задание № 2')

a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

length_of_list: int = len(a)
store_id = id(a)

for _ in range(length_of_list):
    elem = a.pop(0)
    if  elem.isdigit() and elem.isalnum():
        a.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        a.append(f'"+{int(elem):02d}"')
    else:
        a.append(elem)
print (a)
print(' '.join(a))