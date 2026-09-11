ports = (22, 80, 443)

print(ports)
print(ports[0])
print(ports[2])

for port in ports:
	print(port)

print(len(ports))
print(80 in ports)
print(8080 in ports)

unique_ports = {22, 80, 443, 80, 22}
print(unique_ports)
print(len(unique_ports))


unique_ports = {22, 80, 443, 80, 22}
unique_ports.add(8080)
unique_ports.add(80)
print(unique_ports)
print(len(unique_ports))


unique_ports.remove(80)
print(unique_ports)
print(len(unique_ports))


unique_ports.discard(9999)
print(unique_ports)


web_ports = {80, 443, 8080}
admin_ports = {22, 443}

all_ports = web_ports.union(admin_ports)
print(all_ports)

common_ports = web_ports.intersection(admin_ports)
print(common_ports)

web_only = web_ports.difference(admin_ports)
print(web_only)

admin_only = admin_ports.difference(web_ports)
print(admin_only)




default_ports = (22, 80, 443)

server_a = {22, 80, 443, 8080}
server_b = {22, 443, 3306}

print(len(default_ports))
print(443 in default_ports)
all_ports = server_a.union(server_b)
print(all_ports)

common_ports = server_a.intersection(server_b)
print(common_ports)

server_a_only = server_a.difference(server_b)
print(server_a_only)




required_ports = (22, 80, 443)

server_x = {22, 80, 443, 8080, 9000}
server_y = {22, 443, 3306, 9000}

print(len(required_ports))
print(80 in required_ports)

all_server_ports = server_x.union(server_y)
print(all_server_ports)

shared_ports = server_x.intersection(server_y)
print(shared_ports)

x_only = server_x.difference(server_y)
print(x_only)

y_only = server_y.difference(server_x)
print(y_only)
