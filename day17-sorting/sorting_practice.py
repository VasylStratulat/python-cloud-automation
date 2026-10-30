# День 17: sorting_practice.py — сортування, key і lambda
# Теми: sorted() і .sort(), reverse, key=, lambda, min/max з key, зріз [:2]
#
# Підказки:
# - sorted(список) — ПОВЕРТАЄ новий відсортований список, старий не змінюється
# - список.sort() — сортує САМ список "на місці" і повертає None
# - reverse=True — сортування у зворотному порядку (від більшого до меншого)
# - key=функція — "сортуй не за самим елементом, а за тим, що поверне функція"
#       sorted(hosts, key=len)       — за довжиною рядка
#       sorted(hosts, key=str.lower) — без різниці між великими і малими літерами
#   Увага: функцію в key передаємо БЕЗ дужок: key=len, а не key=len()
# - lambda — коротка функція в один рядок, без def і без return:
#       def get_cpu(server):                     get_cpu = lambda server: server["cpu"]
#           return server["cpu"]          ==
#   Читається: "lambda що_приймає: що_повертає"
# - max(список, key=...) / min(список, key=...) — найбільший / найменший за key
# - список[:2] — перші 2 елементи (зріз, slice)


# --- 17.1 sorted() і .sort() ---
ports = [8080, 22, 443, 80]
# a) Надрукуй sorted(ports), а потім сам ports — подивись, чи змінився він
# b) Надрукуй ports, відсортовані від більшого до меншого (reverse)
# c) Відсортуй ports через .sort() і надрукуй ports
# d) Надрукуй результат print(ports.sort()) — що вийшло?
#
# Очікуваний вивід:
# [22, 80, 443, 8080]
# [8080, 22, 443, 80]
# [8080, 443, 80, 22]
# [22, 80, 443, 8080]
# None
#
# Питання (дай відповідь коментарем): чому в пункті d вийшло None?

# Твоє рішення:
# a)
print(sorted(ports))
print(ports)
# b)
print(sorted(ports, reverse=True))
# c)
ports.sort()
print(ports)
# d)
print(ports.sort())
#Бо сортування відбувається "на місці" і повертає None

# --- 17.2 Сортування рядків і key ---
hosts = ["web10", "Web02", "db01", "web2"]
# a) Надрукуй sorted(hosts) без key
# b) Відсортуй без різниці між великими і малими літерами (key=str.lower)
# c) Відсортуй за довжиною імені (key=len)
#
# Очікуваний вивід:
# ['Web02', 'db01', 'web10', 'web2']
# ['db01', 'Web02', 'web10', 'web2']
# ['db01', 'web2', 'web10', 'Web02']
#
# Питання (дай відповідь коментарем): чому "web10" стоїть ПЕРЕД "web2", хоча 10 > 2?

# Твоє рішення:
# a)
print(sorted(hosts))
# b)
print(sorted(hosts, key=str.lower))
# c)
print(sorted(hosts, key=len))
# Бо сортування відбувалось таким чином: Перші три символи однакові далі 
# на четвертому "1" менше за "2", тому web10 іде першим,
# що далі стоїть 0, вже неважливо: рішення ухвалено на першій відмінності.

# --- 17.3 Сортування словників: def і lambda ---
servers = [
    {"name": "web01", "cpu": 45},
    {"name": "web02", "cpu": 92},
    {"name": "db01", "cpu": 30},
    {"name": "cache01", "cpu": 67},
]
# a) Напиши функцію get_cpu(server), яка повертає cpu сервера.
#    Відсортуй servers за cpu через key=get_cpu і надрукуй ТІЛЬКИ імена (comprehension)
# b) Те саме, але через lambda замість get_cpu, і від більшого cpu до меншого
# c) Відсортуй за ім'ям (lambda) і надрукуй імена
#
# Очікуваний вивід:
# ['db01', 'web01', 'cache01', 'web02']
# ['web02', 'cache01', 'web01', 'db01']
# ['cache01', 'db01', 'web01', 'web02']

# Твоє рішення:
# a)
def get_cpu(server):
    return server["cpu"]
by_cpu = sorted(servers, key=get_cpu)
print([server["name"] for server in by_cpu])
# b)
by_cpu_desc = sorted(servers, key=lambda server: server["cpu"], reverse=True)
print([server["name"] for server in by_cpu_desc])
# c)
by_name_desc = sorted(servers, key=lambda server: server["name"])
print([server["name"] for server in by_name_desc])

# --- 17.4 min / max і топ-N ---
# Використай servers з 17.3
# a) Знайди сервер з НАЙБІЛЬШИМ cpu через max(..., key=lambda ...), надрукуй його ім'я
# b) Знайди сервер з НАЙМЕНШИМ cpu через min(...), надрукуй у форматі нижче
# c) Знайди 2 найбільш завантажені сервери (сортування + зріз [:2]), надрукуй їх імена
#
# Очікуваний вивід:
# web02
# db01: 30%
# ['web02', 'cache01']

# Твоє рішення:
# a)
cpu_max = max(servers, key=lambda server: server["cpu"])
print(cpu_max["name"])
# b)
cpu_min = min(servers, key=lambda server: server["cpu"])
print(f"{cpu_min['name']}: {cpu_min['cpu']}%")
# c)
sort_cpu_max = sorted(servers, key=lambda server: server["cpu"], reverse=True)
top_2 = sort_cpu_max[:2]
print([server["name"] for server in top_2])
# --- 17.5 Звіт і логи ---
counts = {"INFO": 2, "WARNING": 1, "ERROR": 3, "DEBUG": 5}
# a) Надрукуй рівні від найчастішого до найрідшого у форматі "DEBUG: 5"
#    (підказка: sorted(counts, ...) перебирає КЛЮЧІ словника;
#     key має повертати кількість для ключа — counts[...])
events = [
    "2026-10-23 10:12:30 ERROR Timeout after 30s",
    "2026-10-23 10:00:01 INFO Server started",
    "2026-10-22 23:59:59 WARNING Disk usage 85%",
    "2026-10-23 10:07:45 ERROR Connection refused",
]
# b) Надрукуй події в хронологічному порядку (від найранішої), кожну з нового рядка
#
# Очікуваний вивід:
# DEBUG: 5
# ERROR: 3
# INFO: 2
# WARNING: 1
# 2026-10-22 23:59:59 WARNING Disk usage 85%
# 2026-10-23 10:00:01 INFO Server started
# 2026-10-23 10:07:45 ERROR Connection refused
# 2026-10-23 10:12:30 ERROR Timeout after 30s
#
# Питання (дай відповідь коментарем): чому в пункті b вистачило звичайного sorted()
# без strptime з дня 16?

# Твоє рішення:
# a)
sorted_level = sorted(counts, key=lambda level: counts[level], reverse=True)
for level in sorted_level:
    print(f"{level}: {counts[level]}")
# b)
sorted_events = sorted(events)
for event in sorted_events:
    print(event)
# Оскільки сортування працє таким чином що воно порівнює значення по черзі то спочатку було сортування по даті
# далі час і так далі тому оскільки потрібно було відсортувати в хронологічному порядку цього вистачило бо спочатку
# йде дата, а потім час в даному списку рядків тому такий порядок нас вланштовує для такого сортування 