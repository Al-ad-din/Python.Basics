from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Валерий', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Богдан', 'Алексей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klass_tutor = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor)
print(type(klass_tutor))
for el in klass_tutor:
    print(el)
