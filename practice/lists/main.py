# Задача 1: Мой план тренировок
workout = ['шрот', 'физика', 'программирование']

workout.append('турники')
workout.sort()
print(workout[0])
print(workout[-1])

print("\n")

# Задача 2: Избавляемся от вредной еды
products = ['хлеб', 'кола', 'творог', 'чипсы', 'яблоки']

products.remove('кола')
del products[2]
print(f"'Полезный' список: {products}")

print("\n")

# Задача 3: Подсчет калорий
calories = [150, 400, 250, 100, 500]

total_sum = 0
for calorie in calories:
    total_sum += calorie

print(f"Общая сумма калорий: {total_sum}")