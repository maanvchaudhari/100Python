import string


def shift_char(char, shift):
    alphabets = (
        list(string.ascii_uppercase) if char.isupper() else list(string.ascii_lowercase)
    )
    new_index = (alphabets.index(char) + shift) % 26
    return alphabets[new_index]


def caesar_cipher(message, operation, shift):
    result = []
    if operation == "decrypt":
        shift *= -1
    for char in message:
        if char.isalpha():
            result.append(shift_char(char, shift))
        else:
            result.append(char)
    print("".join(result))


def main():
    message = input("Enter the message\n→ ")
    # Enter operation
    operation = input("Do you want encrypt or decrypt this message\n→ ").lower()
    while operation not in ("encrypt", "decrypt"):
        operation = input("Do you want encrypt or decrypt this message\n→ ").lower()
    # Enter shift value
    while True:
        try:
            shift = int(input("Enter shift value\n→ "))
            break
        except ValueError:
            print("⚠️ Invalid input given")
    caesar_cipher(message, operation, shift)


if __name__ == "__main__":
    main()
