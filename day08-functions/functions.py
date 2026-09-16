def multiply_numbers(a, b):
    result = a * b
    return result

product = multiply_numbers(4, 5)

print(product)
print(product + 10)


def check_server_status(status):
    if status == "running":
        return "Server is online"
    else:
        return "Server is offline"

result1 = check_server_status("running")
result2 = check_server_status("stopped")

print(result1)
print(result2)


def check_port(port):
    if  port in (22, 80, 443):
        return "Allowed"
    else:
        return "Blocked"

print(check_port(443))
print(check_port(8080))


def check_access(role):
    if role == "admin":
        return "Full access"
    elif role == "user":
        return "Limited access"
    else:
        return "No acces"

print(check_access("admin"))
print(check_access("user"))
print(check_access("guest"))

def calculate_total(a, b):
    total = a + b
    return total

result = calculate_total(10, 15)
print(result)


environment = "production"

def show_environment():
    print("Environment:", environment)

show_environment()


environment = "production"

def change_environment():
    environment = "staging"
    print("Inside:", environment)

change_environment()

print("Outside:", environment)


environment = "production"

def change_global_environment():
    global environment
    environment = "development"

change_global_environment()

print("Global environment:", environment)


def server_info(name, status, port):
    print("Name:", name)
    print("Status:", status)
    print("Port:", port)

server_info(
    port=443,
    name="web-02",
    status="running"
)


def create_user(username, role, active):
    print("Username:", username)
    print("Role:", role)
    print("Active:", active)

create_user(
    role = "admin",
    username = "Vasyl",
    active = True
)


def get_user_info():
    username = "vasyl"
    role = "admin"
    return username, role

user_name, user_role = get_user_info()

print(user_name)
print(user_role)


def get_server_info():
    name = "db-01"
    ip = "10.0.0.50"
    status = "running"
    return name, ip, status
name, ip, status = get_server_info()

print(name)
print(ip)
print(status)


def calculate_server_load(cpu, memory):
    average = (cpu + memory) / 2
    if average >= 80:
        status = "High load"
    elif average >= 50:
        status = "Medium load"
    else:
        status = "Low load"
    return average, status

average, status = calculate_server_load(70, 90)

print(average)
print(status)


server_list = ["web-01", "db-01", "backup-01", "monitoring-01"]

def show_servers(servers):
     for server in servers:
         print(server)

show_servers(server_list)

def count_servers(servers):
     return len(servers)
total = count_servers(server_list)
print ("Total servers:", total)


server = {
    "name": "web-01",
    "ip": "10.0.0.10",
    "status": "running"
}

def show_server_info(server):
    for key, value in server.items():
        print (f"{key}: {value}")

show_server_info(server)



def get_server_status(server):
    return server.get("status", "unknown")

status = get_server_status(server)

print("Server status:", status)


def change_server_status(server, new_status):
    server["status"] = new_status
    return server

updated_server = change_server_status(server, "stopped")

print(updated_server)


def change_server_ip(server, new_ip):
    server["ip"] = new_ip
    return server
updated_server = change_server_ip(server, "10.0.0.25")

print(updated_server)
