# День 16: datetime_practice.py — дата і час
# Теми: datetime, strftime (дата -> текст), strptime (текст -> дата),
#       timedelta (різниця в часі), час у лог-файлах
#
# Підказки:
# - from datetime import datetime, timedelta — підключити потрібне
# - datetime(2026, 10, 27, 14, 5, 9) — створити дату: рік, місяць, день, година, хв, сек
# - datetime.now() — поточні дата і час (щоразу різні!)
# - dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second — окремі частини
# - strftime("формат") — дата -> ТЕКСТ   (f = format, "зроби текст")
# - datetime.strptime(текст, "формат") — ТЕКСТ -> дата   (p = parse, "розбери текст")
# - Коди формату:
#       %Y — рік (2026)    %m — місяць (10)   %d — день (27)
#       %H — година (14)   %M — хвилини (05)  %S — секунди (09)
#   Увага: %m — місяць, %M — хвилини (велика/мала літера важлива!)
# - Дата мінус дата = timedelta (проміжок часу)
# - td.total_seconds() — проміжок у секундах, td.days — у днях
# - dt + timedelta(hours=2) — дата через 2 години (є ще days=, minutes=, seconds=)
# - Дати можна порівнювати: dt1 > dt2 — чи dt1 пізніше
# - items[-1] — ОСТАННІЙ елемент списку, items[0] — перший


from datetime import datetime, timedelta


# --- 16.1 Створення дати і strftime ---
# a) Створи дату dt = 27 жовтня 2026, 14:05:09 і надрукуй її
# b) Надрукуй окремо рік і годину
# c) Надрукуй дату у форматі "27.10.2026 14:05" через strftime()
# d) (без очікуваного виводу) надрукуй datetime.now() — подивись, що вийде
#
# Очікуваний вивід (без пункту d):
# 2026-10-27 14:05:09
# 2026
# 14
# 27.10.2026 14:05

# Твоє рішення:
#a)
dt = datetime(2026, 10, 27, 14, 5, 9)
print(dt)
#b)
print(dt.year)
print(dt.hour)
#c)
print(dt.strftime("%d.%m.%Y %H:%M"))

#d)
print(datetime.now())

# --- 16.2 strptime: текст -> дата ---
text = "2026-10-23 10:07:45"
# a) Перетвори text на дату через datetime.strptime(), збережи у parsed
#    (формат має точно повторювати text: "%Y-%m-%d %H:%M:%S")
# b) Надрукуй type(parsed) і хвилини з parsed
# c) Надрукуй тільки час у форматі "10:07"
#
# Очікуваний вивід:
# <class 'datetime.datetime'>
# 7
# 10:07

# Твоє рішення:
#a)
parsed = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
#b)
print(type(parsed))
print(parsed.minute)
#c)
print(parsed.strftime("%H:%M"))

# --- 16.3 timedelta: різниця в часі ---
# a) Перетвори на дати start = "2026-10-23 10:00:01" і end = "2026-10-23 10:12:30"
# b) Порахуй diff = end - start, надрукуй diff, diff.total_seconds() і type(diff)
# c) Надрукуй, яка дата буде через 2 години після start
#
# Очікуваний вивід:
# 0:12:29
# 749.0
# <class 'datetime.timedelta'>
# 2026-10-23 12:00:01

# Твоє рішення:
# a)
start = "2026-10-23 10:00:01"
end = "2026-10-23 10:12:30"
date_start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
date_end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
# b)
diff = date_end - date_start
print(diff)
print(diff.total_seconds())
print(type(diff))
# c)
new_hours = date_start + timedelta(hours=2)
print(new_hours)
# --- 16.4 Час у логах ---
log_lines = [
    "2026-10-23 10:00:01 INFO Server started\n",
    "2026-10-23 10:05:12 WARNING Disk usage 85%\n",
    "2026-10-23 10:07:45 ERROR Connection refused\n",
    "2026-10-23 10:10:00 INFO Request handled\n",
    "2026-10-23 10:12:30 ERROR Timeout after 30s\n",
]
# a) Напиши функцію parse_time(line), яка повертає дату-час рядка логу як datetime
#    (підказка: розріж як у 14.4, склей date і time через пробіл, потім strptime)
# b) Надрукуй, скільки часу пройшло між ПЕРШИМ і ОСТАННІМ рядком логу
# c) Через comprehension збери повідомлення рядків, що були ПІЗНІШЕ 10:06:00
#    (створи межу border = datetime(2026, 10, 23, 10, 6, 0) і порівнюй з нею)
#
# Очікуваний вивід:
# 0:12:29
# ['Connection refused', 'Request handled', 'Timeout after 30s']

# Твоє рішення:
#a)
def parse_time(line):
    date, time, level, message = line.strip().split(" ", 3)
    date_time = (f"{date} {time}")
    return datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
#b)
diff = parse_time(log_lines[-1]) - parse_time(log_lines[0])
print(diff)
#c)
border =  datetime(2026, 10, 23, 10, 6, 0)
border_time = [line.strip().split(" ", 3)[3] for line in log_lines if parse_time(line) > border]
print(border_time)

# --- 16.5 DevOps-задачі ---
# a) Напиши функцію backup_name(moment), яка повертає ім'я архіву у форматі
#    "backup_РРРРММДД_ГГХХ.tar.gz". Виклич для datetime(2026, 10, 27, 3, 0) і надрукуй
# b) Сертифікат сайту діє до expires = datetime(2026, 11, 5). Сьогодні — today = datetime(2026, 10, 27)
#    Порахуй, скільки днів лишилось (.days), надрукуй число.
#    Якщо менше 14 — надрукуй попередження як у виводі нижче, інакше — "OK"
#
# Очікуваний вивід:
# backup_20261027_0300.tar.gz
# 9
# WARNING: certificate expires in 9 days
#
# Питання (дай відповідь коментарем): чому в 16.5 b ми не використали datetime.now()?

# Твоє рішення:
# a)
def backup_name(moment):
    return f"backup_{moment.strftime('%Y%m%d_%H%M')}.tar.gz"
print(backup_name(datetime(2026, 10, 27, 3, 0)))
# b)
today = datetime(2026,10,27)
expired = datetime(2026,11,5)
days_left = (expired - today).days
print(days_left)
if days_left < 14:
    print(f"WARNING: certificate expires in {days_left} days")
else:
    print("OK")
# Бо ми задавали значення сьогоднішній даті але якщо б нам необхідно було використовувати поточну дату та час то можна було  
# б використати і datetime.now() і в такому випадку наступного дня результат був би іншим відповідно