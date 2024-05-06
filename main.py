import os
import random


clear = lambda: os.system("cls")


print('Привет, я загадал слово твоя задача отгадать его по буквам!')
input('*нажми enter чтобы продолжить*')
clear()
print("Поехали!")

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
# word = words[random.randint(0, len(words) - 1)]
word = random.choice(words)
letters = []

win = True
hp = 10

while hp > 0:
    win = True
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
            win = False
    print()

    if win:
        print("Молодец ты выйграл")
        break

    letter = input("Введите букву: ")
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
    print(f"Осталось попыток {hp}")

if hp == 0:
    print("Ты проиграл")