# День 15: comprehensions.py — list comprehension і dict comprehension
# Теми: короткий запис циклу "порожній список + for + append",
#       фільтр через if, comprehension для словника
#
# Підказки:
# - Ти вже багато разів писав такий шаблон:
#       result = []
#       for x in items:
#           result.append(ЩО_ДОДАТИ)
#   Його можна записати ОДНИМ рядком:
#       result = [ЩО_ДОДАТИ for x in items]
# - З умовою:
#       result = []                          result = [x for x in items if УМОВА]
#       for x in items:
#           if УМОВА:            ->
#               result.append(x)
# - Читай справа наліво: "для кожного x у items, якщо УМОВА, — візьми ЩО_ДОДАТИ"
# - Квадратні дужки [ ] -> вийде список; фігурні { } з key: value -> вийде словник:
#       {КЛЮЧ: ЗНАЧЕННЯ for x in items}
# - Елемент списку за номером: parts[3] — четвертий елемент (рахунок з 0)
#
# Порада: якщо comprehension не виходить — спершу напиши звичайний цикл,
# переконайся, що він працює, а потім "згорни" його в один рядок.


# --- 15.1 Перший comprehension ---
ports = [80, 443, 8080, 22]
# a) Зроби список, де кожен порт перетворено на рядок (str), надрукуй
# b) Зроби список адрес "10.0.0.5:<порт>" для кожного порту (f-рядок), надрукуй
#
# Очікуваний вивід:
# ['80', '443', '8080', '22']
# ['10.0.0.5:80', '10.0.0.5:443', '10.0.0.5:8080', '10.0.0.5:22']

# Твоє рішення:
str_ports = [str(port) for port in ports]
print(str_ports)
ports_adress = [f"10.0.0.5:{port}" for port in ports]
print(ports_adress)
# --- 15.2 Згорни свої старі цикли ---
# a) У дні 12.5 ти писав такий цикл. Перепиши його ОДНИМ рядком через comprehension:
#       lines = []
#       for server in servers_names:
#           lines.append(server + "\n")
servers_names = ["web01", "web02", "db01"]
# b) Почисти кожне ім'я в raw_hosts: прибери пробіли/"\n" і переведи в нижній регістр
#    (підказка: методи можна писати ланцюжком, як у 14.4)
raw_hosts = ["  WEB01 ", "web02\n", " Db01"]
#
# Очікуваний вивід:
# ['web01\n', 'web02\n', 'db01\n']
# ['web01', 'web02', 'db01']

# Твоє рішення:
lines = [f"{server}\n" for server in servers_names]
print(lines)
result_hosts = [host.strip().lower() for host in raw_hosts] 
print(result_hosts)

# --- 15.3 Comprehension з if ---
files = ["app.log", "config.json", "error.log", "backup.tar.gz", "notes.txt"]
servers = [
    {"name": "web01", "cpu": 45, "online": True},
    {"name": "web02", "cpu": 92, "online": True},
    {"name": "db01", "cpu": 30, "online": False},
]
# a) Тільки файли, що закінчуються на ".log" (як у 14.3, але одним рядком)
# b) Імена серверів, які online І мають cpu більше 80 (як у 13.3 c, але одним рядком)
# c) Список значень cpu усіх серверів (без умови)
#
# Очікуваний вивід:
# ['app.log', 'error.log']
# ['web02']
# [45, 92, 30]

# Твоє рішення:
#a)
log_files = [file for file in files if file.endswith(".log")]
print(log_files)
#b
true_servers = [server["name"] for server in servers if server["online"] and server["cpu"] > 80]
print(true_servers)
#c
cpu_servers = [server["cpu"] for server in servers]
print(cpu_servers) 
# --- 15.4 Логи одним рядком ---
log_lines = [
    "2026-10-23 10:00:01 INFO Server started\n",
    "2026-10-23 10:05:12 WARNING Disk usage 85%\n",
    "2026-10-23 10:07:45 ERROR Connection refused\n",
    "2026-10-23 10:10:00 INFO Request handled\n",
    "2026-10-23 10:12:30 ERROR Timeout after 30s\n",
]
# a) Збери у список ТІЛЬКИ повідомлення (message) з ERROR-рядків
#    (підказка: line.strip().split(" ", 3) дає 4 частини, message — під номером [3];
#     перевірити, що це ERROR-рядок, можна через " ERROR " in line)
# b) Збери у список усі рядки, де є " ERROR " АБО " WARNING ", і надрукуй
#    тільки їх КІЛЬКІСТЬ
#
# Очікуваний вивід:
# ['Connection refused', 'Timeout after 30s']
# 3

# Твоє рішення:
#a)
error_line = [line.strip().split(" ", 3)[3] for line in log_lines if "ERROR" in line]
print(error_line)
#b)
count = [line for line in log_lines if "ERROR" in line or "WARNING" in line]
print(len(count))
# --- 15.5 Dict comprehension ---
# Використай список servers з 15.3
# a) Зроби словник {ім'я: cpu} для кожного сервера, надрукуй
# b) Зроби словник {ім'я: online} для кожного сервера, надрукуй
#
# Очікуваний вивід:
# {'web01': 45, 'web02': 92, 'db01': 30}
# {'web01': True, 'web02': True, 'db01': False}
#
# Питання (дай відповідь коментарем): що визначає, чи вийде список, чи словник?

# Твоє рішення:
#a 
servers_cpu = {server["name"] :server["cpu"] for server in servers}
print(servers_cpu)
#b
servers_cpu = {server["name"]: server["online"] for server in servers}
print(servers_cpu)
# Залежить від використання дужок якщо ми використаємо {} то вийде словник але в даному випадку
# всередині дужок має бути пара: ключ та значення бо одне значення дає множину, а якщо [] то вийде список
