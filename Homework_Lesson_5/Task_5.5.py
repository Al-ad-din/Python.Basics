src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 23, 39]
print(src)

unique = []
repeat = []

for el in src:
    if el in repeat:
        continue
    if el in unique:
        repeat.append(el)
        unique.remove(el)
        continue
    unique.append(el)

print(unique)