import random

print("----------Угадай моё число----------")
print("Вам нужно угадать число, выбранное загадочным компьютером")
print("Число в диапазоне от 1 до 1000")

comp_number = random.randint(1, 10)

count = 0
user_number = 0

while user_number != comp_number:
    user_number = int(input())
    count += 1
    if user_number > comp_number:
        print("Число больше загаданного")
    elif user_number < comp_number:
        print("Число меньше загаданного")
    else:
        print("Угадал!!! Потрачено попыток:", count)
game = input("Хотите съиграть снова? Если да, введите - yes, если нет, введите - no: ")

while game != 'no':
    print("----------Угадай моё число----------")
    print("Вам нужно угадать число, выбранное загадочным компьютером")
    print("Число в диапазоне от 1 до 10")

    comp_number = random.randint(1, 10)

    count = 0
    user_number = 0

    while user_number != comp_number:
        user_number = int(input())
        count += 1
        if user_number > comp_number:
            print("Число больше загаданного")
        elif user_number < comp_number:
            print("Число меньше загаданного")
        else:
            print("Угадал!!! Потрачено попыток:", count)
    game = input("Хотите съиграть снова? Если да, введите - yes, если нет, введите - no: ")


            

