# Обратный отсчет с сюрпризом
timer = 10
while timer >= 1:
    if timer == 5 :
        print(f"{timer} : уже половина!")
    else:
        print(timer)
    timer = timer - 1

print("Пуск!")

# Простая касса
total = 0
price = 1
while price != 0:
    price = int(input("Введите цену товара:"))
    total = total + price
    if price == 0:
        break
print(f"Итого к оплате: {total}")

# Эхо-бот с характером
word = ""
while word != "хватит":
    word = input("Скажи что-нибудь:")
    if word == "привет":
        print("И тебе привет!")
    elif word == "хватит":
        print("До встречи!")
    else:
        print(word)

# Банкомат
balanse = 500
cash = 1
while balanse > 0 and cash != 0:
    print(f"Ваш баланс: {balanse}")
    print("Сколько хотите снять?")
    cash = int(input())
    if cash > balanse:
        print("Недостаточно средств!")
    elif cash > 0 :
        balanse = balanse - cash
        print("Возьмите деньги")
    else:
        print("До свидания!")

