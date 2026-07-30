# Задача 1: Мутация vs Переприсваивание
gear = ['шлем', 'броня']

def upgrade_gear_1(items):
    items.append('сапоги')

def upgrade_gear_2(items):
    items = ['легендарный меч', 'щит']

upgrade_gear_1(gear)
print(gear)
upgrade_gear_2(gear)
print(gear)
print("\n")


# Задача 2: Вложенные структуры
player_1 = {'name' : 'Алекс', 'skills' : ['атака', 'защита']}
player_2 = player_1.copy()
player_2['name'] = 'Боб'
player_2['skills'].append('магия')
print(player_1)
print(player_2)