import random, time
from traceback import print_tb


def play_round(user_choise, computer_choise):
    if user_choise == computer_choise:
        return "Ничья!"

    # Проверяем условия победы игрока
    elif (user_choise == "камень" and computer_choise == "ножницы") or \
         (user_choise == "ножницы" and computer_choise == "бумага") or \
         (user_choise == "бумага" and computer_choise == "камень") :
         return "Вы выиграли этот раунд!"
    else :
        return "Вы проиграли этот раунд("

# Главный цикл игры
print("--- ДОБРО ПОЖАЛОВАТЬ В ИГРУ КАМЕНЬ-НОЖНИЦЫ-БУМАГА---")

while True:
    # 1. Ход игрока
    user = input("\nВведите ваш ход(камень, ножницы, бумага) или 'выход' чтобы выйти:").lower()
    if user == 'выход':
        print("Cпасибо за игру! До свидания.")
        break
    if user not in ('камень', 'ножницы', 'бумага'):
        print("Неверный ввод. Попробуйте еще раз!")
        continue

    time.sleep(0.8)

    # 2. Ход компьютера
    print("\nКомпьютер сжимает кулак ... ")
    time.sleep(1.0)
    number = random.randint(1, 3)
    if number == 1:
        comp = "камень"
    elif number == 2:
        comp = "ножницы"
    else:
        comp = "бумага"

    print(f"Компьютер выбрал: {comp}")
    time.sleep(0.8)

    # 3. Определение победителя раунда
    result = play_round(user, comp)
    print(result)

    print("\n" + "="*30)
    time.sleep(2.5)