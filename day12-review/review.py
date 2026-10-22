# День 12: review.py — повторення прогалин
# Теми: set, and/or/not, return кількох значень, scope,
#       writelines/readlines/readline, except ... as error + finally
#
# Підказки:
# - set() прибирає дублікати. Операції: a & b (спільне), a - b (тільки в a), a | b (усе разом)
# - set не має порядку — для стабільного виводу використовуй sorted(...)
# - and: обидві умови True; or: хоча б одна; not: перевертає True/False
# - return a, b, c повертає кортеж; розпаковка: x, y, z = func()
# - змінна, якій присвоюють значення всередині функції, — ЛОКАЛЬНА для цієї функції
# - writelines() НЕ додає "\n" сам — додай його до кожного рядка
# - readlines() повертає список рядків (з "\n"), readline() — лише один рядок
# - except ValueError as error: — у error лежить текст помилки
# - finally виконується ЗАВЖДИ: і після помилки, і навіть після return


# --- 12.1 Множини (set) ---
# Є два списки серверів (з дублікатами):
prod = ["web01", "web02", "db01", "web01", "cache01"]
staging = ["web02", "db01", "test01", "db01"]
# a) Унікальні сервери prod (відсортовано)
# b) Сервери, які є в обох середовищах
# c) Сервери, які є тільки в prod
# d) Скільки всього різних серверів в обох середовищах разом
#
# Очікуваний вивід:
# ['cache01', 'db01', 'web01', 'web02']
# ['db01', 'web02']
# ['cache01', 'web01']
# 5

# Твоє рішення:
print(sorted(set(prod)))
print(sorted(set(prod) & set(staging)))
print(sorted(set(prod) - set(staging)))
total = len(set(prod) | set(staging))
print(total)
# --- 12.2 and / or / not ---
# Напиши функцію check_server(cpu, memory, online), яка ПОВЕРТАЄ статус:
#   - сервер не online                     -> "DOWN"
#   - cpu більше 90 АБО memory більше 90   -> "CRITICAL"
#   - cpu більше 70 І memory більше 70     -> "WARNING"
#   - інакше                               -> "OK"
# Виклич її для: (50, 40, True), (95, 30, True), (75, 80, True), (75, 40, True), (10, 10, False)
#
# Очікуваний вивід:
# OK
# CRITICAL
# WARNING
# OK
# DOWN

# Твоє рішення:
def check_server(cpu, memory, online):
    if online == False:
        return "DOWN"
    elif cpu > 90 or memory > 90:
        return "CRITICAL"
    elif cpu > 70 and memory > 70:
        return "WARNING"
    else:
        return "OK"
print(check_server(0, 40, True))
print(check_server(95, 30, True))
print(check_server(75, 80, True))
print(check_server(75, 40, True))
print(check_server(10, 10, False))
# --- 12.3 Повернення кількох значень ---
# Напиши функцію get_stats(numbers), яка повертає ТРИ значення:
# мінімум, максимум і середнє (округлене до 1 знаку).
# Розпакуй результат у три змінні й надрукуй одним f-рядком.
response_times = [120, 85, 300, 95, 150]
#
# Очікуваний вивід:
# Fastest: 85 ms, slowest: 300 ms, average: 150.0 ms

# Твоє рішення:
def get_stats(numbers):
    low = min(numbers)
    high = max(numbers)
    average = sum(numbers) / len(numbers)
    average = round(average, 1)
    return low, high, average

fastest, slowest, average = get_stats(response_times)
print(f"Fastest: {fastest} ms, slowest: {slowest} ms, average: {average} ms")

# --- 12.4 Область видимості (scope) ---
# Цей код падає з UnboundLocalError. Розкоментуй, запусти, подивись на помилку.
# Потім виправ БЕЗ global: функція має приймати total параметром і повертати нове значення.
# Виклич її 3 рази й надрукуй результат.
#
# total = 0
#
# def add_request():
#     total = total + 1
#
# add_request()
# print(total)
#
# Очікуваний вивід після виправлення:
# Total requests: 3

# Твоє рішення:
total = 0
def add_request(total):
    return total + 1
total = add_request(total)
total = add_request(total)
total = add_request(total)
print(f"Total requests: {total}")



# --- 12.5 writelines / readlines / readline ---
servers = ["web01", "web02", "db01"]
# a) Запиши servers у файл day12_servers.txt через writelines() — кожен з нового рядка
# b) Прочитай файл через readlines(), надрукуй сам список і кількість рядків
# c) Надрукуй сервери з номерами (без зайвих порожніх рядків)
# d) Відкрий файл ще раз і прочитай ТІЛЬКИ перший рядок через readline(), надрукуй його через repr()
#
# Очікуваний вивід:
# ['web01\n', 'web02\n', 'db01\n']
# 3
# 1. web01
# 2. web02
# 3. db01
# 'web01\n'

# Твоє рішення:
lines = []
for server in servers:
    lines.append(server + "\n")

with open("day12_servers.txt", "w") as file:
    file.writelines(lines)
with open("day12_servers.txt", "r") as file:
    result = file.readlines()
print(result)
len_serv = len(result)
print(len_serv)
for number, server in enumerate(result, 1):
    print(f"{number}. {server.strip()}")
with open("day12_servers.txt", "r") as file:
    oneline = file.readline()
    print(repr(oneline))

# --- 12.6 except ... as error + finally ---
# a) Створи кодом два файли: day12_port.txt з текстом "8080" і day12_bad_port.txt з текстом "abc"
# b) Напиши функцію read_port(filename), яка:
#    - читає файл і повертає порт як int
#    - FileNotFoundError -> друкує "File error: <текст помилки>"
#    - ValueError        -> друкує "Value error: <текст помилки>"
#    - у finally завжди друкує "Check finished: <filename>"
# c) Виклич її для "day12_port.txt", "missing.txt", "day12_bad_port.txt"
#    і щоразу друкуй "Port:", результат
#
# Очікуваний вивід:
# Check finished: day12_port.txt
# Port: 8080
# File error: [Errno 2] No such file or directory: 'missing.txt'
# Check finished: missing.txt
# Port: None
# Value error: invalid literal for int() with base 10: 'abc'
# Check finished: day12_bad_port.txt
# Port: None
#
# Питання (дай відповідь коментарем): чому "Check finished" друкується ПЕРЕД "Port: 8080"?

# Твоє рішення:
with open("day12_port.txt", "w") as file:
    file.write("8080")
with open("day12_bad_port.txt", "w") as file:
    file.write("abc")
def read_port(filename):
    try:
        with open(filename, "r") as file:
            port = file.readline()
            return int(port)
    except FileNotFoundError as error:
        print(f"File error: {error}")
    except ValueError as error:
        print(f"Value error: {error}")
    finally:
         print(f"Check finished: {filename}")

print("Port:", read_port("day12_port.txt"))
print("Port:", read_port("missing.txt"))
print("Port:", read_port("day12_bad_port.txt"))
# Оскільки виконується спершу функція яку ми викликаємо тому вивід "Check finished" друкується ПЕРЕД "Port: 8080" тобто цей вивід ствоїть всередині фунції 
# і тому результат функції буде передано лише після її повного виконання. НУ і також finally буде виконуватись завжи навіть після помилки чи return.