# Космический трекер Илона Маска

import math, time

def calculate_distance(x, y):
    distance = x**2 + y**2
    total_distance = math.sqrt(distance)
    return total_distance

target_x = int(input("Введите Х:"))
target_y = int(input("Введите Y:"))
remains = calculate_distance(target_x, target_y)

while remains > 0:
    print(f"Ракета летит ... Осталось {math.ceil(remains)}у.е.")
    time.sleep(1)
    remains -= 1

print("Ракета успешно достигла цели!")