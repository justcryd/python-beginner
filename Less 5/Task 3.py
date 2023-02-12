word_one = input('Введите первое слово: ')
word_two = input('Введите второе слово: ')

if set(word_one) == set(word_two):
    print(f'Слова {word_one} и {word_two} состоят из одних и тех же букв.')
else:
    print('Введенных слова содержат различный набор букв.')
