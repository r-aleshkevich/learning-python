# Система учета тренировок
workout = {"подтягивания" : 15,
           "отжимания"    : 40,
           "приседания"    : 70
           }

# Основной блок выражений
def workout_1(x):
    total_sum = 0
    max_repeats = -1
    volume_training = ""
    for workout_2, repeats in x.items():
        print(f"Тренировка: {workout_2}, повторения - {repeats}")
        total_sum += repeats
        if repeats > max_repeats:
            volume_training = workout_2
            max_repeats = repeats
    print(f"\nОбщая сумма повторений: {total_sum}")
    print(f"Тренировка с самым большим кол-вом повторений: {volume_training}")

# Вызов функции
workout_1(workout)