# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква {word[-1]}')
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'Количество буква А: {word.lower().count("а")}')
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
vovels = "аяуюоеёэиы"
i=0
for w in word:
    if w.lower() in vovels:
        i+=1
print(f'Количество гласных: {i}')
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'В предложении {len(sentence.split())} слова')
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sen = [print(s[0]) for s in sentence.split()]
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
length_sum = 0
sen = sentence.split()
for x in sen:
    length_sum+=len(x)
print(length_sum/len(sen))

# ???