def printMax(a , b):
    if a > b:
        print(f"{a} максимально")
    elif a == b:
        print(f"{a} равно {b}")
    else:
        print(f"{b} максимально")

printMax( 3 , 4) # прямая предача значений

x = 5
y = 7

printMax(x , y) # передача переменных в качестве аргументов