# Генератор кибер-квестов
import random

# Список локаций
locations = ['Северные башни', 'Подпольный клуб', 'Заброшенный склад']

# Словарь целей и награды за них (в кредитах)
targets = {'взлом сервера'  : 500,
           'кража данных'   : 300,
           'зачистка дрона' : 400
           }

def generate_quest(loc_list, target_dict):
    # Выбираем локацию
    location = random.choice(loc_list)

    # Превращаем пары словаря в список и выбираем одну пару(цель, награда)
    target_pair = random.choice(list(target_dict.items()))

    # Распаковываем пару
    task_name, reward = target_pair
    all = (location, task_name, reward)
    return all

def print_quest(quest):
    loc, task, reward = quest
    print(f"Задание: {task} | : {loc} | Награда: {reward} кредитов")

for i in range(1,4):
    print(f"Задание: {i}")
    current_guest = generate_quest(locations, targets)
    print_quest(current_guest)
    print("\n")
