def odd_numbers_gen(num):
    for n in range(1, num + 1, 2):
        yield n


odd_to_numbers = odd_numbers_gen(15)
print(next(odd_to_numbers))
print(next(odd_to_numbers))
print(next(odd_to_numbers))
print(*odd_to_numbers)
print(odd_to_numbers)
