count = 0

with open("servers.txt", "r") as file:
    for line in file:
        print(line.strip())
        count += 1

print("Total servers:", count)

with open("report.txt", "w") as file:
    file.write(f"Total servers: {count}\n")

with open("report.txt", "a") as file:
    file.write("Status: completed\n")

with open("test.txt", "w") as file:
    file.write("First line\n")

with open("test.txt", "a") as file:
    file.write("Second line\n")


with open("servers.txt", "r") as file:
    lines = file.readlines()

servers = []

for line in lines:
    servers.append(line.strip())

print(servers)


with open("clean_servers.txt", "w") as file:
    for server in servers:
        file.write(server + "\n")

server_lines = []

for server in servers:
    server_lines.append(server + "\n")

with open("servers_copy.txt", "w") as file:
    file.writelines(server_lines)

with open("servers.txt", "r") as file:
    first_server = file.readline()
    second_server = file.readline()

print(first_server.strip())
print(second_server.strip())

def load_servers(filename):
    servers = []

    with open(filename, "r") as file:
        for line in file:
            servers.append(line.strip())

    return servers

loaded_servers = load_servers("servers.txt")
print(loaded_servers)

def count_servers_in_file(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            count += 1
    return count
total = count_servers_in_file("servers.txt")
print("Servers in file:", total)


def count_valid_servers(filename):
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                count += 1

    return count

valid = count_valid_servers("servers.txt")
print("Valid servers:", valid)

def load_valid_servers(filename):
    servers = []

    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                servers.append(line.strip())

    return servers

valid_servers = load_valid_servers("servers.txt")
print(valid_servers)


def save_servers(filename, servers):
    with open(filename, "w") as file:
        for server in servers:
            file.write(server + "\n")

save_servers("valid_servers.txt", valid_servers)
