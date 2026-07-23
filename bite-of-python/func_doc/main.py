def printMax(x, y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми цислами.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(f"{x} наибольшее")
    else:
        print(f"{y} наибольшее")

printMax(3, 5)
print(printMax.__doc__)
