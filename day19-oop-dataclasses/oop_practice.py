# День 19: oop_practice.py — ООП, частина 2
# Теми: __str__, @dataclass, значення за замовчуванням, наслідування (основа)
#
# Підказки:
# - __str__(self) — "як надрукувати об'єкт". Python викликає його САМ у print(obj) і f"{obj}".
#   Має ПОВЕРТАТИ рядок (return), а не друкувати:
#       def __str__(self):
#           return f"Dog {self.name}"
#       print(rex)   # Dog Rex   (а без __str__ було б <__main__.Dog object at 0x...>)
#
# - @dataclass — скорочений запис класу для зберігання даних. __init__ пише Python сам!
#       from dataclasses import dataclass      # ← один раз на початку файлу
#
#       @dataclass
#       class Dog:
#           name: str          # поле: назва і тип (str — текст, int — ціле число, bool — True/False)
#           age: int
#
#       rex = Dog("Rex", 3)
#       print(rex)             # Dog(name='Rex', age=3)   ← гарний друк теж автоматично
#   Значення за замовчуванням:  age: int = 1   (поля з "=" пишуться ПІСЛЯ полів без "=")
#   Методи в dataclass пишуться так само, як у звичайному класі (з self)
#
# - Наслідування:  class Puppy(Dog):  — Puppy отримує ВСЕ від Dog (__init__, методи)
#   і може ПЕРЕВИЗНАЧИТИ (написати заново) будь-який метод.
#   isinstance(obj, Клас) — True, якщо obj створено з цього класу або з його нащадка

from dataclasses import dataclass


# --- 19.1 __str__ ---
# Створи звичайний клас Product (name, price) як учора, і додай метод __str__,
# який повертає рядок у форматі "Laptop (25000 грн)".
# p = Product("Laptop", 25000)
# a) Надрукуй p
# b) Надрукуй f-рядок "Order item: {p}"
#
# Очікуваний вивід:
# Laptop (25000 грн)
# Order item: Laptop (25000 грн)

# Твоє рішення:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} ({self.price} грн)"
p = Product("Laptop", 25000)
print(p)
print(f"Order item: {p}")

# --- 19.2 Перший dataclass ---
# Створи dataclass User з полями name (str), email (str), age (int).
# u = User("Olha", "olha@example.com", 30)
# a) Надрукуй u
# b) Надрукуй email користувача
# c) Надрукуй результат порівняння u == User("Olha", "olha@example.com", 30)
#
# Очікуваний вивід:
# User(name='Olha', email='olha@example.com', age=30)
# olha@example.com
# True

# Твоє рішення:
@dataclass
class User:
    name: str
    email: str
    age: int
u = User("Olha", "olha@example.com", 30)
print(u)
print(u.email)
print(u == User("Olha", "olha@example.com", 30))
# --- 19.3 Значення за замовчуванням + метод ---
# Створи dataclass Task з полями title (str) і done (bool, за замовчуванням False).
# Додай метод complete(), який змінює done на True.
# t = Task("Write tests")      ← done не передаємо!
# Надрукуй t.done, потім виклич t.complete() і надрукуй t
#
# Очікуваний вивід:
# False
# Task(title='Write tests', done=True)

# Твоє рішення:
@dataclass
class Task:
    title: str
    done: bool = False
    def complete(self):
        self.done = True
t = Task("Write tests")
print(t.done)
t.complete()
print(t)

# --- 19.4 Список dataclass-об'єктів ---
# Створи dataclass Item з полями name (str), price (int), in_stock (bool, за замовчуванням True).
# items = [Item("Laptop", 25000), Item("Mouse", 500, False), Item("Keyboard", 1200)]
# a) Надрукуй імена товарів, які Є в наявності (comprehension з if)
# b) Надрукуй суму цін товарів, які є в наявності (sum + comprehension з if)
# c) Надрукуй НАЙДЕШЕВШИЙ товар цілком (min + key) — подивись, як гарно він друкується
#
# Очікуваний вивід:
# ['Laptop', 'Keyboard']
# 26200
# Item(name='Mouse', price=500, in_stock=False)

# Твоє рішення:
@dataclass
class Item:
    name: str
    price: int
    in_stock: bool = True
items = [Item("Laptop", 25000), Item("Mouse", 500, False), Item("Keyboard", 1200)] 
stock = [item.name for item in items if item.in_stock]
print(stock)
items_price = sum(item.price for item in items if item.in_stock)
print(items_price)
chipest = min(items, key=lambda item: item.price)
print(chipest)
# --- 19.5 Наслідування ---
# Створи звичайний клас Account:
#   __init__(self, name) — зберігає name
#   role(self) — повертає "user"
#   info(self) — повертає f"{self.name} ({self.role()})"
# Створи клас AdminAccount(Account), у якому є ТІЛЬКИ метод role(), що повертає "admin".
# acc = Account("Olha"), adm = AdminAccount("Ivan")
# Надрукуй acc.info(), adm.info(), isinstance(adm, Account)
#
# Очікуваний вивід:
# Olha (user)
# Ivan (admin)
# True
#
# Питання (дай відповідь коментарем): в AdminAccount ми не писали ні __init__, ні info().
# Звідки вони взялися, і чому adm.info() надрукував "admin", а не "user"?

# Твоє рішення:
class Account:
    def __init__(self, name):
        self.name = name
    def role(self):
        return "user"
    def info(self):
        return f"{self.name} ({self.role()})"    
class AdminAccount(Account):
    def role(self):
        return "admin"
acc = Account("Olha")
adm = AdminAccount("Ivan")
print(acc.info())
print(adm.info())
print(isinstance(adm, Account))
# Оскільки class AdminAccount унаслідував методи з class Account так як після class AdminAccount в дужкаї (Account) тобто унаслідування з якого класу. 
# adm.info() надрукував "admin", а не "user" оскільки було використано другий клас який повертає лише значення адмін так як він знайшов
# це значення(метод в даному випадку) і йогму не потрібно було звертатись до класу від якого вібувалось наслідування 