# Система управления космостанцией

log_entry = "SYSTEM_STATUS:ONLINE:SECTOR_ALPHA"
if log_entry.startswith('SYSTEM_STATUS'):
    print('Да, лог-запрос начинается на: "SYSTEM_STATUS"')

print(f'Название сектора: {log_entry[22:]}')
print('\n')

# Сканер двух отсеков нашел редкие минералы
compartment_1 = set(['уран', 'титан', 'лед', 'уран'])
compartment_2 = set(['золото', 'титан', 'медь'])

unique_minerals = compartment_1 | compartment_2
print(f"Все уникальные элементы с 2 отсеков: {unique_minerals}")
intersec_min = compartment_1 & compartment_2
print(f"Минералы, которые есть и в 1, и во 2 отсеке: {intersec_min}")
print("\n")

# Cловарь с прочностью
systems = {'щиты' : 80, 'двигатель' : 45, 'связь' : 95, 'кислород' : 60}
def analyze_systems(sys_dict):
    max_strength = -1
    min_strength = 999
    max_device = ""
    min_device = ""
    for device, strength in sys_dict.items():
        if strength > max_strength:
            max_strength = strength
            max_device = device

        if strength < min_strength:
            min_strength = strength
            min_device = device

    return (max_device, min_device)

best_sys, worst_sys = analyze_systems(systems)
print(f"Лучшая сиcтема: {best_sys}, Худшая система: {worst_sys}")

# Создаем копию systems
systems_backup = systems.copy()
systems['щиты'] = 0
print(f"Оригинал с поломкой: {systems}")
print(f"Цэлый бэкап: {systems_backup}")




