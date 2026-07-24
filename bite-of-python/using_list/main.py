# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print(f"Я должен сделать {len(shoplist)} покупок.")

print("Покупки:", end =" ")
for item in shoplist:
    print(item, end=" ")

print("\nТакже нужно купить риса.")
shoplist.append("рис")
print(f"Теперь мой список покупок таков: {shoplist}")

print("Отсортирую-ка я свой список")
shoplist.sort()
print(f"Отсортированный список покупок таков: {shoplist}")

print(f"Первое, что мне нужно купить, это {shoplist[0]}")
olditem = shoplist[0]
del shoplist[0]
print(f"Я купил {olditem}")
print(f"Теперь мой список покупок: {shoplist}")