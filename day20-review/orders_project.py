# День 20: orders_project.py — повторення, міні-проєкт "Замовлення інтернет-магазину"
# Збираємо разом: dataclass + методи + __str__, рядки (split), функції з return,
# comprehension з if, підрахунок у словнику (.get), max/sorted з key, JSON, try/except
#
# Це одна програма: кожен наступний пункт використовує результат попереднього.
# Пиши код по черзі, зверху вниз, і перевіряй після кожного пункту.
#
# Нагадування (усе це ти вже робив):
# - "1;Olha;Laptop".split(";")           → ['1', 'Olha', 'Laptop']   (день 14)
# - int("25000")                         → 25000 (з тексту в число)
# - counts[k] = counts.get(k, 0) + 1     — підрахунок у словнику (день 14)
# - [x for x in items if умова]          — comprehension з фільтром (день 15)
# - sorted(..., key=lambda ..., reverse=True)[:3]  — топ-3 (день 17)
# - json.dump(дані, f, indent=2) / json.load(f)    — запис / читання JSON (день 13)
# - try: ... except FileNotFoundError: ...         — обробка помилок (день 12)

import json
from dataclasses import dataclass


# --- 20.1 Модель замовлення ---
# Створи dataclass Order з полями:
#   id (int), customer (str), product (str), price (int), quantity (int), status (str, за замовчуванням "new")
# Методи:
#   total(self)   — повертає price * quantity
#   __str__(self) — повертає рядок у форматі "#1 Olha: Laptop x1 = 25000 грн"
#                   (сума — через виклик self.total())
# Перевірка: o = Order(1, "Olha", "Laptop", 25000, 1, "paid"); print(o)
#
# Очікуваний вивід:
# #1 Olha: Laptop x1 = 25000 грн

# Твоє рішення:
@dataclass
class Order:
    id: int
    customer: str
    product: str
    price: int
    quantity: int
    status: str = "new"
    def total(self):
        total = self.price * self.quantity  
        return total
    def __str__(self):
        return f"#{self.id} {self.customer}: {self.product} x{self.quantity} = {self.total()} грн"
            
o = Order(1, "Olha", "Laptop", 25000, 1, "paid"); print(o)

# --- 20.2 Розбір "сирих" даних ---
# Замовлення прийшли текстом (як із файлу або старої системи):
raw = [
    "1;Olha;Laptop;25000;1;paid",
    "2;Ivan;Mouse;500;3;new",
    "3;Olha;Keyboard;1200;2;paid",
    "bad line",
    "4;Petro;Monitor;7000;1;cancelled",
    "5;Ivan;Laptop;25000;1;paid",
]
# a) Напиши функцію parse_order(line):
#      - розбиває рядок по ";"
#      - якщо частин НЕ 6 → повертає None (зламаний рядок)
#      - інакше → повертає Order(...) (не забудь int() для id, price, quantity)
# b) Пройдись циклом по raw: успішні замовлення додавай у список orders,
#    а зламані рядки рахуй у змінній skipped
# c) Надрукуй підсумок і перше замовлення зі списку
#
# Очікуваний вивід:
# Parsed 5 orders, skipped 1
# #1 Olha: Laptop x1 = 25000 грн

# Твоє рішення:
def parse_order(line):
    splited_line = line.split(";")
    if len(splited_line) != 6:
        return None
    else:
        return Order(int(splited_line[0]), splited_line[1], splited_line[2], int(splited_line[3]), 
    int(splited_line[4]), splited_line[5])
orders = []
skipped = 0
for line in raw:
    order = parse_order(line)
    if order is None:
        skipped += 1
    else:
        orders.append(order)
print(f"Parsed {len(orders)} orders, skipped {skipped}")
print(orders[0])
# --- 20.3 Звіти ---
# a) Збери список paid — лише замовлення зі статусом "paid" (comprehension з if).
#    Надрукуй виручку — суму total() оплачених замовлень
# b) Порахуй кількість замовлень кожного статусу у словник (по ВСІХ orders) і надрукуй його
# c) Порахуй, скільки ВИТРАТИВ кожен клієнт (лише paid) у словник {клієнт: сума},
#    знайди того, хто витратив найбільше (max + key), і надрукуй
#
# Очікуваний вивід:
# Revenue: 52400 грн
# {'paid': 3, 'new': 1, 'cancelled': 1}
# Top customer: Olha (27400 грн)

# Твоє рішення:
paid = [order for order in orders if order.status == "paid"]
prices = sum(order.total() for order in paid)
print(f"Revenue: {prices} грн")
count = {}
for order in orders:
    count[order.status] = count.get(order.status, 0) + 1
print(count)
spent = {}
for order in paid:
    spent[order.customer] = spent.get(order.customer, 0) + order.total()
top = max(spent, key=lambda name: spent[name])
print(f"Top customer: {top} ({spent[top]} грн)")
# --- 20.4 Топ-3 замовлення за сумою ---
# Відсортуй УСІ orders за total() від більшого до меншого, візьми перші 3
# і надрукуй кожне з нового рядка (print(order) — спрацює твій __str__)
#
# Очікуваний вивід:
# #1 Olha: Laptop x1 = 25000 грн
# #5 Ivan: Laptop x1 = 25000 грн
# #4 Petro: Monitor x1 = 7000 грн

# Твоє рішення:
by_total = sorted(orders, key=lambda order: order.total(), reverse=True)
top3 = by_total[:3]
for order in top3:
    print(order)
# --- 20.5 Збереження в JSON і читання назад ---
# a) Запиши у файл day20_orders.json список словників для КОЖНОГО paid-замовлення:
#      {"id": ..., "customer": ..., "total": ...}     (comprehension, що створює словники)
#    Увага: json не вміє записувати об'єкти Order напряму — тільки словники, списки, числа, рядки
# b) Прочитай файл назад, надрукуй кількість записів і список імен клієнтів
# c) Спробуй прочитати файл day20_missing.json (його немає!) — злови помилку через try/except
#    і надрукуй повідомлення
#
# Очікуваний вивід:
# 3
# ['Olha', 'Olha', 'Ivan']
# File not found: day20_missing.json
#
# Питання (дай відповідь коментарем): чому parse_order повертає None для зламаного рядка,
# а не просто друкує "помилка"? Що це дає коду, який її викликає?

# Твоє рішення:
orders_jason = [{"id": order.id, "customer": order.customer, "total": order.total()} for order in paid]
with open("day20_orders.json", "w") as file:
    json.dump(orders_jason, file, indent=2)
with open("day20_orders.json", "r") as file:
    load = json.load(file)
    count_client = len(load)
    print(count_client)
    names = [record["customer"] for record in load]
    print(names)
try:
    with open("day20_missing.json", "r") as file:
        json.load(file)
except FileNotFoundError:
    print("File not found: day20_missing.json")
# Бо при написанні функції було прямо зазначено що якщо рядок зламаний треба повертатити None. Тому це так і працює.
# І це зроблено було для того щоб програма не падала із за однієї полимлки і проджовжувала працювати при цьому буде
#  ще й запис про те що було пропущено рядок.