print("Простое присваивание")
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь еще одно имя, указывающее на объект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю ее

print(f'shoplist: {shoplist}')
print(f'mylist: {mylist}')
# shoplist и mylist выводят один и тот же список без пункта "яблоки",
# подтверждая тем самым, что они указывают на один объект

print("Копирование при помощи вырезки")
mylist = shoplist[:] # создаем копию путем полной вырезки
del mylist[0]

print(f"shoplist: {shoplist}")
print(f"mylist: {mylist}")
# обратим внимание, что теперь списки разные