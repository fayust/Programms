import random

alph = ('b', 'a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

length = random.randint(0,4)
word = []
userword = []
for i in range(length):
    userword.append('_')
count = 0

for i in range(length):
    word += random.choice(alph)

while userword != word:
    count += 1
    print('Введите букву:')
    lt = input()

    try:
        if  lt not in alph:
            raise IndexError('нет в словаре')
        elif lt not in word:
             print('Эта буква отсутствует в загаданном слове')
        else:
            for i in range(len(word)):
                if word[i] == lt:
                    userword[i] =lt
                    print('Угаданные буквы слова: {}'.format(str(userword)))
    except IndexError:
            print("Эта буква отсутствует в словаре")

if userword == word:
    print('Вы отгадали слово {} за {} попыток'.format(word, count))