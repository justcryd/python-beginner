if set(word_one := input("Введите первое слово: ")) == set(word_two := input
    ("Введите второе слово: ")):
    print(f'Слова {word_one} и {word_two} состоят из одних и тех же букв.')
else:
    print('Введенные слова содержат различный набор букв.')
