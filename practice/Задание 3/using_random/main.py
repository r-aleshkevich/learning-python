import random

secret_number = random.randint(1,100)

print("Я загадал число от 1 до 100 Попробуй угадать!")

while True:
    user_guess = int(input("Введите свой вариант:"))

    if user_guess == secret_number:
        print("Ура! Ты угадал!")
        break
    else:
        print("Мимо!")