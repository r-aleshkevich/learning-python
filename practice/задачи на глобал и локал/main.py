# Счетчик жизней

lives = 3
def lose_life(lives):
    lives-=1
    print(lives)

lose_life(lives)
print(lives)

#Взломщик банка

money = 500

def steal_money():
    global money

    money = 0

steal_money()
print(money)

# Локальный калькулятор

def square(num):
    num *= num
    print(num)

square(5)
