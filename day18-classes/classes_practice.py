# День 18: classes_practice.py — класи і об'єкти (ООП, частина 1)
# Теми: class, __init__, self, атрибути, методи, список об'єктів
#
# Підказки:
# - class — це КРЕСЛЕННЯ (шаблон). Об'єкт — конкретна річ, зроблена за кресленням.
#       креслення "Товар"  →  об'єкти: ноутбук за 25000, мишка за 500
# - Створення класу:
#       class Product:
#           def __init__(self, name, price):   # викликається САМ при створенні об'єкта
#               self.name = name               # зберегти name ВСЕРЕДИНІ об'єкта
#               self.price = price
# - Створення об'єкта:  p = Product("Laptop", 25000)   ← self НЕ передаємо, Python підставить сам
# - self — "цей конкретний об'єкт". self.name — "ім'я САМЕ ЦЬОГО товару"
# - Атрибут (дані) — БЕЗ дужок:   p.name, p.price
#   Метод (дія)    — З дужками:   p.info()
# - Метод — це функція всередині класу. Першим параметром ЗАВЖДИ self:
#       def info(self):
#           return f"{self.name}: {self.price}"
# - Увага на відступи: методи пишемо З ВІДСТУПОМ всередині class,
#   а створення об'єктів і print — БЕЗ відступу, після класу


# --- 18.1 Перший клас ---
# a) Створи клас Product з атрибутами name і price (через __init__)
# b) Створи два об'єкти: p1 = Laptop за 25000, p2 = Mouse за 500
# c) Надрукуй ім'я p1 і ціну p2
# d) Зміни ціну p2 на 450 (просто присвоєнням) і надрукуй її знову
#
# Очікуваний вивід:
# Laptop
# 500
# 450

# Твоє рішення:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name}: {self.price} грн"
    def discounted(self, percent):
        return self.price * (100 - percent) // 100
p1 = Product("Laptop", 25000)
p2 = Product("Mouse", 500)
keyboard = Product("Keyboard", 1200)
print(p1.name)
print(p2.price)
p2.price = 450
print(p2.price)
print(p1.info())
print(keyboard.info())
print(p1.discounted(10))
# --- 18.2 Методи ---
# Додай у клас Product з 18.1 (прямо в нього, нижче __init__) два методи:
# a) info() — ПОВЕРТАЄ рядок у форматі "Laptop: 25000 грн"
# b) discounted(percent) — ПОВЕРТАЄ ціну зі знижкою: price * (100 - percent) // 100
# Створи keyboard = Product("Keyboard", 1200) і надрукуй:
#   p1.info(), keyboard.info(), p1.discounted(10)
#
# Очікуваний вивід:
# Laptop: 25000 грн
# Keyboard: 1200 грн
# 22500

# Твоє рішення:


# --- 18.3 Кошик: об'єкт, що зберігає інші об'єкти ---
# Створи клас Cart:
#   __init__(self) — створює порожній список self.items = []
#   add(self, product) — додає товар у self.items
#   count(self) — повертає кількість товарів
#   total(self) — повертає суму цін усіх товарів
# Створи кошик, додай у нього p1 і keyboard, надрукуй:
#   count(), total(), і список імен товарів у кошику (comprehension по cart.items)
#
# Очікуваний вивід:
# 2
# 26200
# ['Laptop', 'Keyboard']

# Твоє рішення:
class Cart:
    def __init__(self):
        self.items = []
    def add(self, product):
        self.items.append(product)
    def count(self):
        return len(self.items)
    def total(self):
        total = 0
        for product in self.items:
            total = total + product.price  
        return total
bascet = Cart()
bascet.add(p1)
bascet.add(keyboard)
print(bascet.count())
print(bascet.total())
print([item.name for item in bascet.items])
# --- 18.4 Стан об'єкта: замовлення ---
# Створи клас Order:
#   __init__(self, order_id) — зберігає order_id, а status одразу = "new"
#   pay(self) — змінює status на "paid"
#   ship(self) — якщо status == "paid", змінює status на "shipped",
#                інакше друкує "Cannot ship: order 101 is not paid" (номер — з order_id)
# Виконай по черзі:
#   order = Order(101) → надрукуй status → order.ship() → order.pay() →
#   надрукуй status → order.ship() → надрукуй status
#
# Очікуваний вивід:
# new
# Cannot ship: order 101 is not paid
# paid
# shipped

# Твоє рішення:
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "new"
    def pay(self):
        self.status = "paid"
    def ship(self):
        if self.status == "paid":
            self.status = "shipped"
        else:
            print(f"Cannot ship: order {self.order_id} is not paid")

order = Order(101)
print(order.status)
order.ship()
order.pay()
print(order.status)
order.ship()
print(order.status)

# --- 18.5 Список об'єктів + сортування з дня 17 ---
# Створи клас User з атрибутами name і age.
# users = [User("Olha", 30), User("Ivan", 25), User("Petro", 41)]
# a) Надрукуй імена всіх користувачів (comprehension)
# b) Надрукуй імена, відсортовані за віком (sorted + key=lambda ...)
# c) Надрукуй ім'я найстаршого (max)
#    Увага: у об'єкта звертаємось user.age, а не user["age"] як у словника
#
# Очікуваний вивід:
# ['Olha', 'Ivan', 'Petro']
# ['Ivan', 'Olha', 'Petro']
# Petro
#
# Питання (дай відповідь коментарем): у def add(self, product) два параметри,
# а викликаємо cart.add(p1) з одним аргументом. Куди подівся self?

# Твоє рішення:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
users = [User("Olha", 30), User("Ivan", 25), User("Petro", 41)]
users_name = [user.name for user in users]
print(users_name)
by_age = sorted(users, key=lambda user: user.age)
print([user.name for user in by_age])
oldest = max(users, key=lambda user: user.age)
print(oldest.name)
#Бо self є параметром  і його Python підставляє сам, а у def add(self, product): product є аргументом  тому фактично один параметр для використання 
# і це product який ми зазначаємо 