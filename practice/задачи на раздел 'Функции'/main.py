# Фитнес-трекер

def create_step_tracker(goal):
    total_steps = 0

    def add_steps(steps):
        nonlocal total_steps
        total_steps += steps

        if total_steps>= goal:
            print(f"Цель достигнута! Вы прошли {total_steps}")
        else:
            left = goal - total_steps
            print(f"Пройдено {total_steps} из {goal}.Осталось пройти {left}")


    return add_steps
my_tracker = create_step_tracker(10000)

my_tracker(5000)
my_tracker(7000)


# Генератор красивых заголовков

def format_header(text, symbol = "-", length = 20):
    '''Функция берет symbol и повторяет его length раз.

       Функция возвращает краисую строку,где сначала идет
       линия из символов, потом на новой строке сам текст,
       а потом снова линия из символов.'''

    return (symbol * length) + "\n" + text + "\n" + (symbol * length)

print(format_header("Я крутой программист"))
print(format_header.__doc__)


# Калькулятор налогов

def create_calculator():
    total_sum = 0
    total_counted = 0

    def calculate_tax(price,*, tax = 13, **kwargs):
        nonlocal total_sum
        nonlocal total_counted

        total_counted += 1
        final =  price + (price * tax / 100)
        if "скидка" in kwargs:
            final -= kwargs["скидка"]

        total_sum += final

        print(f"Текущий подсчет №: {total_counted}")
        print(f"Стоимость этого товара: {final}")
        print(f"Общая сумма всех товаров: {total_sum}")
        print("-" * 20) # Просто красивая линия

    return calculate_tax
calculation = create_calculator()
calculation(100)
calculation(100, скидка = 10)