# Система авторизации

def check_password(password):
    if password == "Python2026":
        return True
    else:
        return False

print("У вас есть 3 попытки,чтобы угадать пароль!")

tries = 0
while tries < 3:
    tries += 1
    guess = input("Введите пароль:")
    if check_password(guess):
        print("Доступ разрешен.")
        break
    else:
        print(f"Не верно! Осталось попыток: {3-tries}")
else:
    print("Аккаунт заблокирован!")

# Угадай число

from random import randint

computer_choice = randint(1, 50)
counter = 0
while True:
    guess = int(input("Угадайте число от 1 до 50:"))
    counter += 1
    if guess == computer_choice:
        print("Вы угадали!")
        break
    elif guess < computer_choice:
        print("Нет, загаданное число немного больше этого.")
    else:
        print("Нет, загаданное число немного меньше этого.")
    print(f"Число ваших попыток: {counter}")

#  Калькулятор времени

def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    final_seconds = remaining_seconds % 60
    return f"{hours}:{minutes}:{final_seconds}"

print(format_time(3665))

# Анализатор текста

text = input("Введите любой текст:").lower()
vowels = 0
consonants = 0
spaces = 0
for letter in text:
    if letter == " ":
        spaces += 1
    elif letter in "аеиоуыэюя":
        vowels += 1
    elif letter.isalpha(): # .isalpha() отсекает все знаки кроме букв
        consonants += 1
print(f"Пробелы:{spaces}. Гласные:{vowels}. Согласные:{consonants}")