# Задача : Анализ тренировок
def analyze_workout(durations):
    # 1. Сортируем список
    durations.sort()

    # 2. Находим мин и макс
    min_duration = durations[0]
    max_duration = durations[-1]

    # 3. Считаем сумму через цикл
    total_sum = 0
    for i in durations:
        total_sum += i

    # 4. Считаем среднее
    average_duration = total_sum / len(durations)

    # 5. Возвращаем кортеж с результатами
    return (min_duration, max_duration, average_duration)

# Создаем список тренировок снаружи функции
my_workouts = [45, 60, 30, 90, 45]

# Вызываем функцию и распаковываем кортеж в 3 переменные
minimal, maximal, average = analyze_workout(my_workouts)

# Выводим результат на экран
print(f"Минимум: {minimal} мин.")
print(f"Максимум: {maximal} мин.")
print(f"Среднее: {average} мин.")

