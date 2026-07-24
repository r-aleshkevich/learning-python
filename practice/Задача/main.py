#Автоматизированная система управления складом
sklad_heavy = 0
sklad_light = 0
total_sum = 0
while True :
    user_input =input("Введите вес коробки (кг) или 'stop': ")
    if user_input == "0" or user_input =="stop":
        break
    weight = int(user_input)
    if weight < 0 or weight > 30 :
        print("Ошибка: вес  может быть от 0 до 30 кг.")
        continue
    if weight <= 10:
        sklad_light += weight
    else:
        sklad_heavy += weight
    total_sum = sklad_heavy + sklad_light
    if total_sum >= 100:
        print("Склад полностью заполнен.Приемка окончена.")
        break
print(f"Принято кг легких товаров: {sklad_light}")
print(f"Принято кг тяжелых товаров: {sklad_heavy}")
print(f"Вcего кг товаров: {total_sum}")
