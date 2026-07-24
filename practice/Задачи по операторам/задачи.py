# Время в пути

total_minutes = 158
hour = total_minutes // 60
minutes= total_minutes % 60
print(f"{hour}ч.{minutes}мин.")

# Школьные парты
students = 27
desks = students // 2
solo_students = students % 2
print(f"{desks} парт, {solo_students} один")

# Зеркальное число
n = 47
a = n // 10
b = n % 10
print(b*10+a)

# Високосный год
year = 2024
year_1 = year % 4
print(year_1==0)

# Среднее геометрическое
a = 8
b = 18
g = (a*b) ** 0.5
print(g)

# Фейсконтроль
age = 19
money = 60
can_enter = (age>=18 and money > 50)
print(f"Пустят ли в клуб ? {can_enter}")

# Скидка
is_saturday = False
has_card = True
a = is_saturday or has_card
print(a)

# Битовый сдвиг
x = 10
y = x << 1
print(y)