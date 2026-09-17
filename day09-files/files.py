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
