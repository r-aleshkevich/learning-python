# MATH
import math

user_guess = float(input("Введите любое дробное число:"))
print(math.sqrt(user_guess))
print(math.floor(user_guess))
print(math.ceil(user_guess))
print("До свидания!")

# RANDOM
from random import randint
programm_guess = randint(1, 5)
guess = int(input("Угадайте число от 1 до 5:"))
if guess == programm_guess :
    print("Поздравляю! Вы угадали.")
elif guess < programm_guess:
    print("Загаданное число немного больше этого.")
else:
    print("Загаданное число немного меньше этого")

#DATETIME
from datetime import date

new_year = date(2026, 12, 31)

today = date.today()
result = new_year - today

print(result.days)