server = {
	"name": "web-01",
	"ip": "192.168.1.10",
	"status": "running"
}

print(server)
print(server["name"])
print(server["ip"])
print(server["status"])

server["status"] = "stopped"

print(server)
print(server["status"])

server["port"] = 80

print(server)
print(server["port"])

removed_port = server.pop("port")

print(removed_port)
print(server)

print(server.get("name"))
print(server.get("location"))
print(server.get("location", "Unknown"))

print(server.keys())
print(server.values())
print(server.items())

for key in server:
	print(key)

for key, value in server.items():
	print(key, value)

for key, value in server.items():
	print(f"{key}: {value}")


cloud_server = {
	"name": "app-01",
	"ip": "10.0.0.25",
	"status": "running",
	"port": 8080
}

cloud_server["status"] = "stopped"
cloud_server["environment"] = "production"
print(cloud_server.get("region", "Unlnown"))
cloud_server.pop("port")
for key, value in cloud_server.items():
	print(f"{key}: {value}")

database_server = {
	"name": "db-01",
	"ip": "10.0.0.50",
	"status": "stopped",
	"port": 5432
}

database_server["status"] = "running"
database_server["environment"] = "staging"
database_server["backup"] = "True"
database_server.pop("port")
print(database_server.get("region", "Not configured"))
for key, value in database_server.items():
	print(f"{key}: {value}")
