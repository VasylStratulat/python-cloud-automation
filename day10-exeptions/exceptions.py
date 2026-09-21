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