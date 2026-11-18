# День 21: main.py — віртуальне оточення (venv), pip і проєкт з кількох файлів
# Теми: python3 -m venv, activate, pip install, requirements.txt, import з власних файлів,
#       if __name__ == "__main__"
#
# Сьогодні частина роботи — в ТЕРМІНАЛІ (у VS Code: Ctrl+` відкриває термінал).
# Команди терміналу позначені знаком $ — сам знак $ НЕ вводь.
#
# Навіщо це все:
# - venv — окрема "коробка" з бібліотеками для ОДНОГО проєкту. У проєкту A може бути
#   FastAPI версії 0.110, у проєкту B — 0.115, і вони не заважають одне одному.
# - pip — програма, що завантажує й встановлює бібліотеки (requests, fastapi, ...) у цю коробку.
# - requirements.txt — СПИСОК бібліотек проєкту. Інший розробник (або сервер) встановить
#   все однією командою: pip install -r requirements.txt
# - Кілька файлів — щоб не тримати все в одному: моделі окремо, допоміжні функції окремо.
#       from models import Product      — "з файлу models.py візьми Product"
#
# Важливо: усі команди виконуй, перебуваючи в папці day21-venv-modules:
#   $ cd ~/python_learning/day21-venv-modules


# --- 21.1 Створення venv ---
# a) У твоєму Ubuntu (WSL) модуль venv ще не встановлено. Встанови його (один раз на комп'ютер,
#    попросить пароль від WSL):
#       $ sudo apt install python3.12-venv
# b) Створи віртуальне оточення в папці .venv:
#       $ python3 -m venv .venv
# c) Активуй його:
#       $ source .venv/bin/activate
#    Зліва в терміналі з'явиться (.venv) — значить, коробка "відкрита"
# d) Виконай $ which python3   і запиши нижче коментарем, який шлях він показав
# e) Виконай $ deactivate   потім знову $ which python3   — і запиши, що змінилося
# f) Знову активуй venv (крок c) — далі працюємо в ньому
#
# Твоя відповідь (коментарем):
# З venv - /home/vasyl/python_learning/day21-venv-modules/.venv/bin/python3
#/usr/bin/python3

# --- 21.2 pip і requirements.txt ---
# (venv має бути активним — (.venv) зліва!)
# a) Встанови бібліотеку requests (знадобиться на дні 23 для HTTP-запитів):
#       $ pip install requests
# b) Подивись, що встановилось:  $ pip list
#    Питання: чому там не лише requests, а ще кілька пакетів? (дай відповідь коментарем)
# c) Збережи список у файл:  $ pip freeze > requirements.txt
#    Відкрий requirements.txt і подивись, що всередині
# d) У VS Code вибери інтерпретатор з venv: Ctrl+Shift+P → "Python: Select Interpreter" →
#    той, що в ./.venv/bin/python  (тоді VS Code не підкреслюватиме import requests)
# e) Нижче в коді: імпортуй requests і надрукуй його версію: requests.__version__
#    Запускай файл з терміналу з активним venv:  $ python main.py
#
# Очікуваний вивід (цифри версії можуть бути іншими):
# requests 2.32.5
#
# Твоя відповідь на питання (коментарем):
# Ймовірно тому що вони належали до папки реквест так як він використовує їх у своїй роботі
# Твоє рішення:

import requests                          
print(f"requests {requests.__version__}") 
# --- 21.3 Проєкт з кількох файлів ---
# a) Створи поруч з main.py файл models.py. У ньому — dataclass Product:
#       name (str), price (int), quantity (int, за замовчуванням 1), метод total() → price * quantity
#    (не забудь у models.py свій import dataclass — кожен файл імпортує те, що йому потрібно)
# b) Створи файл utils.py з двома функціями:
#       format_price(amount)   → повертає рядок "26500 грн"
#       cart_total(products)   → повертає суму total() усіх товарів у списку
# c) Тут, у main.py, імпортуй Product з models, а format_price і cart_total — з utils.
#    Створи products = [Product("Laptop", 25000), Product("Mouse", 500, 3)]
#    Надрукуй кількість товарів і загальну суму через format_price(cart_total(...))
#
# Очікуваний вивід (разом з 21.2):
# requests 2.32.5
# 2
# 26500 грн

# Твоє рішення:
from models import Product
from utils import format_price, cart_total
products = [Product("Laptop", 25000), Product("Mouse", 500, 3)]
print(len(products))
print(format_price(cart_total(products)))
# --- 21.4 if __name__ == "__main__" ---
# a) В КІНЕЦЬ utils.py додай рядок (без відступу):
#       print("Testing utils:", format_price(100))
#    Запусти $ python main.py — що з'явилось у виводі, хоча в main.py такого print немає?
# b) Тепер "сховай" цей print під умову:
#       if __name__ == "__main__":
#           print("Testing utils:", format_price(100))
#    Запусти $ python main.py  і  $ python utils.py  — порівняй вивід
#
# Очікуваний вивід:
#   $ python main.py   → як у 21.3 (без "Testing utils")
#   $ python utils.py  → Testing utils: 100 грн
#
# Питання (дай відповідь коментарем): що робить Python з файлом utils.py, коли бачить
# from utils import ... ? І навіщо тоді потрібен if __name__ == "__main__"?
#
# Твоя відповідь (коментарем):
# Python виконує повністю зазначений файл в даному випадку utils.py і передає нам уже необхідне нам значення які ми зазначежмо після імпорту.
# Це потрібно для того щоб вивід який є тестовим не виводився якщо ми його викликаєм через файл main

# --- 21.5 Git: що зберігати, а що ні ---
# Виконай $ git status (з папки python_learning). Ти побачиш папку .venv серед нових файлів.
# Питання (дай відповідь коментарем): чому .venv НЕ комітять у git, а requirements.txt — комітять?
# Підказка: подивись, скільки важить .venv:  $ du -sh .venv
#
# Твоя відповідь (коментарем):
# Бо папка важить 19Mb і окрім того ще 644 файли  тому немає сенсу її комітити оскільки requirements.txt це вже список бібліотек і маючи такий можна його викорстати 
# для створення такого самого оточення однією командою pip install -r (назва в нашому випалку це requirements.txt)