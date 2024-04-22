import os

clear = lambda: os.system("cls")


print('Привет, я загадал слово твоя задача отгадать его по буквам!')
input('*нажми enter чтобы продолжить*')
clear()
print("Поехали!")

word = "слон"
letters = []

win = True
hp = 10

while hp > 0:
    win = True
    letter = input("Введите букву: ")
    letters.append(letter)
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

    if letter not in word:
        hp -= 1
        print(f"Осталось попыток {hp}")