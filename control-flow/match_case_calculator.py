try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input for the first number. Please enter a valid number.")
    exit()
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input for the second number. Please enter a valid number.")
    exit()
operation = input("Choose the operation (+, -, *, /): ").strip()

result = None
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
        