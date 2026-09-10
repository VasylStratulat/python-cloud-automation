total = 0
count = 0

while True:
	number = int(input("Enter a number: "))
	if number == 0:
		break
	if number < 0:
		continue

	total = total + number
	count = count + 1

print("Total:",total)
print("Count:",count)
