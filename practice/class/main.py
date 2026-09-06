# Задание 1
class Car:
    def beep(self):
        print("Би-би!")

my_car = Car()
my_car.beep()

# Задание 2
class Car:
    def __init__(self, brand):
        self.brand = brand

myCar = Car("Volvo")
print(myCar.brand)

# Задание 3
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self,damage):
        self.hp -= damage
        print(f"Герой {self.name} получил {damage} урона! Осталось HP: {self.hp}")

hero = Hero("Артур", 100)
hero.take_damage(30)

# Задание 4
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery
    def play_game(self,minutes):
        self.battery -= minutes * 2
        print(f"Ocталось заряда: {self.battery}%")
    def charge(self):
        self.battery = 100
        print(f"{self.model} полностью заряжен!")
phone = Phone("iPhone 17", 100)
phone.play_game(20)
phone.charge()

# Задание 5
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Новый баланс: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Снято {amount} руб. Остаток: {self.balance} руб.")
        else:
            print("Недостаточно средств!")

myacc = BankAccount("Роман", 3500)
myacc.deposit(270)
myacc.withdraw(1350)
