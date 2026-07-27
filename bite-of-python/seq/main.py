shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print(f"Элемент 0 - {shoplist[0]}")
print(f"Элемент 1 - {shoplist[1]}")
print(f"Элемент 2 - {shoplist[2]}")
print(f"Элемент 3 - {shoplist[3]}")
print(f"Элемент -1 - {shoplist[-1]}")
print(f"Элемент -2 - {shoplist[-2]}")
print(f"Символ 0 - {name[0]}")

# Вырезка из списка
print(f"Элементы с 1 по 3: {shoplist[1:3]}")
print(f"Элементы с 2 до конца: {shoplist[2:]}")
print(f"Элементы с 1 по -1: {shoplist[1:-1]}")
print(f"Элементы от начала до конца: {shoplist[:]}")

# Вырезка из строки
print(f"Символы с 1 по 3: {name[1:3]}")
print(f"Символы с 2 до конца: {name[2:]}")
print(f"Символы с 1 до -1: {name[1:-1]}")
print(f"Символы от начала до конца: {name[:]}")