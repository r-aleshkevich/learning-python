# Задача 1: Дешифровка сигнала
signal = "WARP-ORION-9982-GRID"

# Название корабля
print(f"Название корабля: {signal[5:10]}")

# Номер сектора
print(f"Номер сектора: {signal[11:15]}")
print("\n")


# Задача 2: Космический радар
scanned_objects = ['астероид','НЛО', 'комета', \
'мусор', 'станция']

# Индекс НЛО
print(f"Индекс НЛО: {scanned_objects.index('НЛО')}")

print(f"Средние объекты: {scanned_objects[1:4]}")
print("\n")


# Задача 3: Умный склад
found_items = ['сталь', 'медь', 'сталь', 'платина', \
'медь', 'никель', 'титан']
unique_objects = set(found_items)

# Проверка на наличие платины
if 'платина' in unique_objects:
    print("Внимание: обнаружен ценный ресурс!")

# Сколько уникальных ресурсов всего собрано
print(f"Собрано уникальных ресурсов: {len(unique_objects)}")
print("\n")


# Задача 4: Совместимость команд
alpha_squad = {'медик', 'штурмовик', 'инженер', 'снайпер'}
bravo_squad = {'штурмовик', 'пилот', 'медик', 'разведчик'}

# Специалисты, которые есть в обеих командах
together_squad = alpha_squad & bravo_squad
print(f" Специалисты, которые есть в обеих командах: {together_squad}")

# Список уникальных специалистов, | = .union
unique_squad = alpha_squad.union(bravo_squad)
print(f"Список уникальных специалистов: {unique_squad}")
print("\n")


# Задача 5: Спец-задание
required = {'топливо', 'навигатор', 'щиты', 'пушки'}
cargo = {'топливо', 'щиты'}

# Недостаток cargo
flaw_cargo = required - cargo
if len(flaw_cargo) == 0:
    print("Прыжок разрешен!")
else:
    print(f"Не хватает компонентов для прыжка: {flaw_cargo}")