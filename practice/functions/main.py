# func_nonlocal

def func_outer():
    x = 2
    print(f"х равно {x}")

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print(f"Локальное х сменилось на {x}")

func_outer()


# func_default

def say(message, times = 1):
    print(message * times)

say("Hi", 10)


#func_key

def func(a, b = 5, c = 10):
    print(f"a равно {a}, b равно {b}, c равно {c}")

func(3,7)
func(25, c= 24) # c - ключевой аргумент
func(c = 50, a = 100) # b получает 5 по умолчанию


# return

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "Числа равны"
    else:
        return y

print(maximum(2, 3))
