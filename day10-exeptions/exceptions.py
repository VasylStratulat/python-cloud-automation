try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
finally:
    print("Program finished")

def divide_numbers():
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1 / number2

    except ValueError:
        print("Please enter valid numbers")    
    except ZeroDivisionError:
        print("Cannot divide by zero")

    else:
        print("Result: ", result)

    finally:
        print("Calculation finished")

divide_numbers()

try:
    with open("existing_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found")

else:
    print(content)

finally:
    print("File operation finished")

def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        return"File not found"
    else:
        return content
print(read_file_safe("existing_file.txt"))
print(read_file_safe("missing_file.txt"))

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except Exception as error:
    print("Error:", error)

else:
    print("Result:", result)

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError as error:
    print("Value error:", error)

except ZeroDivisionError as error:
    print("Division error:", error)

else:
    print("Result:", result)

def read_number_from_file(filename):
    try:
        with open(filename, "r") as file:
            number = int(file.read().strip())
    except FileNotFoundError:
        return "File not found"
    except ValueError:
        return "Invalid number"
    return number

print(read_number_from_file("port.txt"))
print(read_number_from_file("bad_port.txt"))
print(read_number_from_file("missing_port.txt"))

def load_port(filename):
    try:
        with open(filename, "r") as file:
            port = int(file.read().strip())
    except FileNotFoundError:
        return "File not found"
    except ValueError:
        return "Invalid port" 
    else:
        return port
    finally:
        print("Port check finished")

print(load_port("port.txt"))
print(load_port("bad_port.txt"))
print(load_port("missing_port.txt"))