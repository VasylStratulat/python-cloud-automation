# День 14: strings_practice.py — методи рядків і розбір логів
# Теми: strip/lower/replace, split/join, startswith/endswith/in,
#       розбір рядків лог-файлу, підрахунок через словник
#
# Підказки:
# - Методи рядків НЕ змінюють рядок, а ПОВЕРТАЮТЬ новий: clean = raw.strip()
# - strip() — прибирає пробіли і "\n" з обох країв
# - lower() / upper() — усе малими / великими літерами
# - replace("що", "на що") — замінює частину рядка ("" — щоб видалити)
# - split(",") — ріже рядок по комі і повертає СПИСОК
# - split(" ", 3) — ріже по пробілу, але не більше 3 разів (решта лишається цілою)
# - ", ".join(список) — склеює список у рядок через ", " (навпаки до split)
# - startswith("abc") / endswith(".log") — повертають True/False
# - "error" in name — чи є частина "error" всередині рядка
# - Методи можна писати ланцюжком: line.strip().split(",")
# - Підрахунок у словнику: counts[key] = counts.get(key, 0) + 1
#   (get(key, 0) повертає поточне значення або 0, якщо ключа ще немає)


# --- 14.1 strip / lower / replace ---
raw = "  Web01.Example.COM  \n"
# a) Прибери пробіли та "\n" з країв, збережи у змінну, надрукуй через repr()
# b) Переведи результат у нижній регістр і надрукуй
# c) Прибери з нього ".example.com" через replace() і надрукуй — має лишитись тільки ім'я
#
# Очікуваний вивід:
# 'Web01.Example.COM' 
# web01.example.com
# web01

# Твоє рішення:
raw = raw.strip()
print(repr(raw))
lower_raw = raw.lower()
print(lower_raw)
replase_raw = lower_raw.replace(".example.com", "")
print(replase_raw)


# --- 14.2 split / join ---
line = "web01,10.0.0.5,8080,online"
# a) Розріж line по комі, збережи список у parts і надрукуй
# b) Розпакуй parts у 4 змінні: name, ip, port, status
#    Надрукуй f-рядком у форматі нижче
# c) Надрукуй type(port). Потім перетвори port на int і надрукуй port + 1
# d) Склей список hosts в один рядок через ", " за допомогою join() і надрукуй
hosts = ["web01", "web02", "db01"]
#
# Очікуваний вивід:
# ['web01', '10.0.0.5', '8080', 'online']
# web01 -> 10.0.0.5:8080
# <class 'str'>
# 8081
# web01, web02, db01

# Твоє рішення:
parts = line.split(",")
print(parts)
name, ip, port, status = parts
print(f"{name} -> {ip}:{port}")
print(type(port))
int_port = int(port)      
new_port = int_port + 1
print(new_port)
join_hosts = ", ".join(hosts)
print(join_hosts)

# --- 14.3 startswith / endswith / in ---
files = ["app.log", "config.json", "error.log", "backup.tar.gz", "notes.txt"]
# a) Збери у список тільки файли, що закінчуються на ".log", надрукуй список
# b) Збери у список файли, в назві яких є "config" АБО які починаються з "backup",
#    надрукуй список
#
# Очікуваний вивід:
# ['app.log', 'error.log']
# ['config.json', 'backup.tar.gz']

# Твоє рішення:
files_log = []
for f in files:
    if f.endswith(".log"):
        files_log.append(f)
print(files_log)

cfg_bak_files = []
for b in files:
    if b.startswith("backup") or "config" in b:
        cfg_bak_files.append(b) 
print(cfg_bak_files)

# --- 14.4 Розбір лог-файлу ---
log_lines = [
    "2026-10-23 10:00:01 INFO Server started\n",
    "2026-10-23 10:05:12 WARNING Disk usage 85%\n",
    "2026-10-23 10:07:45 ERROR Connection refused\n",
    "2026-10-23 10:10:00 INFO Request handled\n",
    "2026-10-23 10:12:30 ERROR Timeout after 30s\n",
]
# a) Запиши log_lines у файл day14_app.log через writelines()
# b) Прочитай файл через readlines(). Для кожного рядка:
#    - прибери "\n" і розріж на 4 частини: date, time, level, message
#      (підказка: split(" ", 3) — щоб повідомлення "Server started" не розрізалось)
#    - якщо level == "ERROR", надрукуй час і повідомлення як у виводі нижче
# c) У тому ж циклі порахуй, скільки рядків кожного рівня, у словнику counts
#    Після циклу надрукуй counts
#
# Очікуваний вивід:
# 10:07:45 Connection refused
# 10:12:30 Timeout after 30s
# {'INFO': 2, 'WARNING': 1, 'ERROR': 2}

# Твоє рішення:
with open("day14_app.log", "w") as file:
    file.writelines(log_lines)
with open("day14_app.log", "r") as file:
    lines = file.readlines()
    counts = {}
    for line in lines:
        strip_lines = line.strip()
        slit_line = strip_lines.split(" ", 3)
        date, time, level, message = slit_line
        if level == "ERROR":
            counts["ERROR"] = counts.get("ERROR", 0) + 1
            print(f"{time} {message}")
        elif level == "WARNING":
            counts["WARNING"] = counts.get("WARNING", 0) + 1
        elif level == "INFO":
            counts["INFO"] = counts.get("INFO", 0) + 1
    print(counts)

# --- 14.5 Функція + звіт у файл ---
# a) Напиши функцію parse_line(line), яка ПОВЕРТАЄ три значення: time, level, message
#    Перевір її: надрукуй parse_line("2026-10-23 10:05:12 WARNING Disk usage 85%")
# b) Використай parse_line() для рядків з 14.4: збери у список тільки ERROR-рядки
#    у форматі "10:07:45 Connection refused\n" і запиши їх у файл day14_errors.txt
# c) Прочитай day14_errors.txt і надрукуй, скільки рядків збережено
#
# Очікуваний вивід:
# ('10:05:12', 'WARNING', 'Disk usage 85%')
# Errors saved: 2
#
# Питання (дай відповідь коментарем): чому у пункті a вивід у круглих дужках?

# Твоє рішення:
def parse_line(line):
    strip_line = line.strip()
    split_line = strip_line.split(" ", 3)
    date, time, level, message = split_line
    return time, level, message
print(parse_line("2026-10-23 10:05:12 WARNING Disk usage 85%"))
errors = []
for line in lines:
    time, level, message = parse_line(line)
    if level == "ERROR":
        errors.append(f"{time} {message}\n")
with open("day14_errors.txt", "w") as file:
    file.writelines(errors)
with open("day14_errors.txt", "r") as file:
    read_lines = file.readlines()
    count_lines = len(read_lines)
print(f"Errors saved: {count_lines}")
# Отримуємо вивід у круглих дужках оскільки вивід від return є кортежем