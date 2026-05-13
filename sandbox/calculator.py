def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    print("* WELCOME TO CALCULATOR *")
    while True:
        try:
            num1 = float(input("Enter the first number\n: "))
            num2 = float(input("Enter the first number\n: "))
            break
        except ValueError:
            print("⚠️ Enter valid numbers\n")
    print("\n", " ".join(operations))
    operation = input("What operation would you like to perform\n: ")
    while operation not in operations:
        print("⚠️ Invalid operation")
        operation = input("What operation would you like to perform\n: ")
    if operations == "/" and num2 == 0:
        print("⚠️ Cannot divide by zero")
    else:
        result = operations[operation](num1, num2)
        print(f"\n{num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    calculator()
