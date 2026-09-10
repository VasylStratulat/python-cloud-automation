servers = ["web", "db", "backup"]
servers.append("monitoring")
servers.insert(1, "api")

print(servers[0])
print(servers[1])
print(servers[2])
print(servers[-1])
print(servers[-2])
print(servers[-3])

servers[2] = "database"
print(servers)

servers.remove("backup")
print(servers)

removed_server = servers.pop(1)
print(removed_server)
print(servers)

print(len(servers))

for server in servers:
	print(server)

for server in servers:
	if server == "database":
		print("Database server found")

print("database" in servers)
print("backup" in servers)

print("backup" not in servers)
print("web" not in servers)


ports = [443, 22, 8080, 80]

ports.sort()
print(ports)

ports.sort(reverse=True)
print(ports)


services = ["web", "api", "database", "bacup", "monitoring"]

print(services[1:4])
print(services[:3])
print(services[2:])
print(services[::2])
print(services[::-1])
print(services.index("database"))
print(services.index("monitoring"))

statuses = ["up", "down", "up", "up", "down"]

print(statuses.count("up"))
print(statuses.count("down"))


servers = ["web", "database", "backup", "monitoring"]

print(len(servers))
for server in servers:
	if server == "database":
		print("Database server found")
servers.append("api")
servers.remove("backup")
for server in servers:
	print(server)
