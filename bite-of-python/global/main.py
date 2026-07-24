x = 50

def func():
    global x

    print(f" x равно {x}")
    x = 2
    print(f" Заменяем глобальное значение х на {x}")

func()
print(f" Значение х составляет {x}")