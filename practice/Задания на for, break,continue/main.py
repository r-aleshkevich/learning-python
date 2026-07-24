# Фильтр чисел
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

#Остановка на цели
total_sum = 0
for i in range(1, 101):
    total_sum += i
    if total_sum > 50:
        break
print(f"Итоговая сумма : {total_sum}")

#Проверка пароля
while True:
    guess = input("Введите слово:")
    if guess == "выход":
        break
    print(f"Вы ввели : {guess}")
print("Завершение")

# Умный калькулятор
for i in range(5, -6, -1):
    if i == 0:
        break
    if i < 0:
        continue
    print(100/i)

#Поиск первого делителя
for i in range(100, 151):
    if i % 7 ==0:
        print(i)
        break
print("Нашел! Завершение.")

#Складской терминал
total_weight = 0
while True:
    weight = int(input("Введите вес :"))
    if weight == 0:
        break
    if weight < 0:
        print("Ошибка: вес не может быть отрицательным.")
        continue
    total_weight += weight
print(f"Вес составляет : {total_weight}")








