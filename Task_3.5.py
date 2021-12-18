print('Задание № 5')

from random import choice


def get_jokes(num=1):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    list_jokes = []
    for joke in range(num):
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return list_jokes


print(get_jokes(num=5))
