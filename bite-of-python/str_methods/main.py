name = 'Swaroop'

if name.startswith('Swa'):
    print('Да, строка  начинается на "Swa"')

if 'a' in name:
    print('Да, строка содержит строку "a"')

if name.find('war') != -1: # лучше использовать if in
    print('Да, строка содержит строку "war"')

delimetr = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimetr.join(mylist))