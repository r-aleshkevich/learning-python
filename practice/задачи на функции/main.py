def computer(battery_kwh, avg_consumption = 18.0, weather_temp = 20):
    current_consumption = avg_consumption
    if weather_temp <0:
        current_consumption *= 1.25
    elif weather_temp > 35:
        current_consumption *= 1.10

    return round((battery_kwh / current_consumption) * 100)

print(f"Запас хода: {computer(20,20, weather_temp= 36)} км")

# Счетчик такси

def taximetr():
    total_earned = 0

    def add_ride(distance, rate_per_km = 0.8, surge_multiplier = 1):
        nonlocal total_earned

        ride_cost = distance * rate_per_km * surge_multiplier
        total_earned += ride_cost

        return (f"Поездка: {ride_cost}р. Всего заработано: {total_earned}р.")
    return add_ride
my_taxi = taximetr()
print(my_taxi(10))
print(my_taxi(20))


# Калькулятор заказов

def calculate_order(*items, delivery = 500, **discounts):
    total = 0
    for item in items:
        total+= item
    for discount in discounts:
        percent = discounts[discount]

        total*= (1- percent / 100)

    return total + delivery

print(calculate_order(20,50,130, promo1 = 20,promo2 = 15))


# Генератор персонажа

def create_hero(*skills, base_hp, ** equipment):
    total_hp = base_hp
    for key in equipment:
        total_hp += equipment[key]
    print(f"Итоговое здоровье(HP) : {total_hp}")
    for skill in skills:
        print(f"-{skill}")

    return total_hp
hero_hp = create_hero("Меч", "Щит", helmet = 20, armor = 50, base_hp = 100)
print(f"Здоровье : {hero_hp} hp")
print("О нет, монстр атакует!")
hero_hp -= 20
print(f"Нынешнее здоровье : {hero_hp} hp")



