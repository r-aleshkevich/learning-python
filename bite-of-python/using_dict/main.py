# 'ab' - сокращение от 'a'ddress'b'ook

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
        }

print(f"Адрес Swaroop'a: {ab['Swaroop']}")

# Удаление пары ключ-значение
del ab['Spammer']

print(f"\nВ адресной книге {len(ab)} контактов\n")

for name, adress in ab.items():
    print(f"Контакт {name} с адресом {adress}")

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print(f"\nАдрес Guido: {ab['Guido']}")
