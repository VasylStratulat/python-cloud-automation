# День 13: json_practice.py — робота з JSON
# Теми: json.dumps / json.loads, json.dump / json.load, список словників у JSON,
#       зміна конфігу, обробка помилок JSON
#
# Підказки:
# - JSON — текстовий формат для даних. Виглядає майже як словник Python, але:
#   рядки ТІЛЬКИ в подвійних лапках "...", True/False -> true/false, None -> null
# - import json — підключити модуль
# - json.dumps(data)  — Python -> рядок JSON   (s = string)
# - json.loads(text)  — рядок JSON -> Python
# - json.dump(data, file, indent=4) — записати у ФАЙЛ (indent=4 — гарні відступи)
# - json.load(file)   — прочитати з ФАЙЛУ
# - Запам'ятай: з "s" на кінці — робота з рядком, без "s" — з файлом
# - Битий JSON дає помилку json.JSONDecodeError


import json


# --- 13.1 dumps / loads ---
server = {"name": "web01", "port": 8080, "online": True}
# a) Перетвори server на рядок JSON через json.dumps(), збережи у змінну й надрукуй
# b) Надрукуй type() цієї змінної
# c) Перетвори рядок назад на словник через json.loads(), надрукуй значення "port"
#    і type() результату
#
# Очікуваний вивід:
# {"name": "web01", "port": 8080, "online": true}
# <class 'str'>
# 8080
# <class 'dict'>
#
# Питання (дай відповідь коментарем): що змінилося з True у виводі пункту a?
# Змінив клас на рядок і перша літера замінилась на маленьку.
# Твоє рішення:
js_server = json.dumps(server)
print(js_server)
print(type(js_server))
back = json.loads(js_server)
print(back["port"])
print(type(back))
# --- 13.2 dump / load у файл ---
config = {"app": "monitor", "version": "1.2", "ports": [80, 443], "debug": False}
# a) Запиши config у файл day13_config.json через json.dump() з indent=4
#    Відкрий файл у VS Code і подивись, як він виглядає
# b) Прочитай файл через json.load() у змінну loaded
# c) Надрукуй: значення "app", ДРУГИЙ порт зі списку "ports", type() списку "ports"
#
# Очікуваний вивід:
# monitor
# 443
# <class 'list'>

# Твоє рішення:
with open("day13_config.json", "w") as file:
    json.dump(config, file, indent=4)
with open("day13_config.json", "r") as file:
    loaded = json.load(file)
    print(loaded["app"])
    print(loaded["ports"][1])
    print(type(loaded["ports"]))


# --- 13.3 Список словників ---
servers = [
    {"name": "web01", "cpu": 45, "online": True},
    {"name": "web02", "cpu": 92, "online": True},
    {"name": "db01", "cpu": 30, "online": False},
]
# a) Запиши servers у файл day13_servers.json (indent=4)
# b) Прочитай файл назад і для кожного сервера надрукуй рядок як у виводі нижче
#    (online/offline залежно від значення "online")
# c) Збери у список імена серверів, які online І мають cpu більше 80, надрукуй список
#
# Очікуваний вивід:
# web01: cpu 45%, online
# web02: cpu 92%, online
# db01: cpu 30%, offline
# ['web02']

# Твоє рішення:
with open("day13_servers.json", "w") as file:
    json.dump(servers, file, indent=4)
with open("day13_servers.json", "r") as file:
    loaded = json.load(file)
    for server in loaded:
        if server["online"]:
            status = "online"
        else:
            status = "offline"
        print(f"{server['name']}: cpu {server['cpu']}%, {status}")
busy = []
for server in loaded:
    if server["online"] and server["cpu"] > 80:
        busy.append(server["name"])
print(busy)



# --- 13.4 Зміна конфігу ---
# a) Прочитай day13_config.json (з 13.2)
# b) Зміни "version" на "1.3", додай порт 8080 у "ports", постав "debug" у True
# c) Запиши змінений конфіг назад у той самий файл (indent=4)
# d) Прочитай файл ще раз і надрукуй увесь словник
#
# Очікуваний вивід:
# {'app': 'monitor', 'version': '1.3', 'ports': [80, 443, 8080], 'debug': True}

# Твоє рішення:

with open("day13_config.json", "r") as file:
    cfg = json.load(file)
    cfg["version"] = "1.3"
    cfg["ports"].append(8080)
    cfg["debug"] = True
with open("day13_config.json", "w") as file:
    json.dump(cfg, file, indent=4)
with open("day13_config.json", "r") as file:
    loaded = json.load(file)
    print(loaded)

# --- 13.5 Помилки JSON ---
# a) Створи кодом файл day13_bad.json з текстом {app: monitor}  (битий JSON — немає лапок)
# b) Напиши функцію load_config(filename), яка:
#    - читає файл через json.load() і повертає словник
#    - FileNotFoundError     -> друкує "File error: <текст помилки>"
#    - json.JSONDecodeError  -> друкує "JSON error: <текст помилки>"
# c) Виклич її для "day13_config.json", "missing.json", "day13_bad.json"
#    і щоразу друкуй "Config:", результат
#
# Очікуваний вивід:
# Config: {'app': 'monitor', 'version': '1.3', 'ports': [80, 443, 8080], 'debug': True}
# File error: [Errno 2] No such file or directory: 'missing.json'
# Config: None
# JSON error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
# Config: None

# Твоє рішення:
with open("day13_bad.json", "w") as file:
    file.write("{app: monitor}")
def load_config(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(f"File error: {error}")
    except json.JSONDecodeError as error:
        print(f"JSON error: {error}")
    
print("Config:", load_config("day13_config.json"))
print("Config:", load_config("missing.json"))
print("Config:", load_config("day13_bad.json"))

