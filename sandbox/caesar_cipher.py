import string


def shift_char(char, shift):
    base = ord("A") if char.isupper() else ord("a")
    char_index = ord(char) - base
    new_index = ((char_index + shift) % 26) + base
    return chr(new_index)


def caesar_cipher(message, operation, shift):
    result = []
    if operation == "decrypt":
        shift *= -1
    for char in message:
        if char.isalpha():
            result.append(shift_char(char, shift))
        else:
            result.append(char)
    return f"\n{operation.capitalize()}ed message: {''.join(result)}"


def main():
    message = input("Enter the message\n→ ")
    # Enter operation
    operation = input("Do you want encrypt or decrypt this message\n→ ").strip().lower()
    while operation not in ("encrypt", "decrypt"):
        operation = (
            input("Do you want encrypt or decrypt this message\n→ ").strip().lower()
        )
    # Enter shift value
    while True:
        try:
            shift = int(input("Enter shift value\n→ "))
            break
        except ValueError:
            print("⚠️ Invalid input given")
    print(caesar_cipher(message, operation, shift))


if __name__ == "__main__":
    main()
