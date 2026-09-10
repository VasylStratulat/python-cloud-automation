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
