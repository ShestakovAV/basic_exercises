# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
word = word.lower()
count = 0
for letter in word:
    if letter in vowel:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
word_list = sentence.split()
print(len(word_list))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
word_list = sentence.split()
for word in word_list:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
word_list = sentence.split()
amount_of_letters = 0
for word in word_list:
    amount_of_letters += len(word) 
print(amount_of_letters/len(word_list))