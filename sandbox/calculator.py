import subprocess


def take_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except:
            print("\t Invalid Input. Enter a numeric value")


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def main():
    subprocess.run(["clear"])
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    n1 = take_number("Enter first number: ")
    while True:
        n2 = take_number("Enter next number: ")
        print("\nAvailable operations: ", ", ".join(operations.keys()))
        operation = input("What operation would you like to perform: ").strip()
        if n2 == 0 and operation == "/":
            print("\tERROR - Divide by zero\n")
            continue
        while operation not in operations:
            print("\tInvalid Input. Select from the operations listed above")
            operation = input("What operation would you like to perform: ").strip()
        result = operations[operation](n1, n2)
        print(f"\n{n1} {operation} {n2} = {result}")
        print("\n[C] Continue calculation\n[F] Fresh calculation\n[E] Exit")
        do_continue = input("What would you like to do: ").strip().lower()
        while do_continue not in ("c", "f", "e"):
            print("\tInvalid choice. Select from the operations listed above.")
            do_continue = input("What would you like to do: ").strip().lower()
        if do_continue == "f":
            main()
        elif do_continue == "e":
            return
        elif do_continue == "c":
            n1 = result
            subprocess.run(["clear"])


if __name__ == "__main__":
    main()
