import string
import subprocess


def shift_char(char, shift):
    alphabets = (
        list(string.ascii_uppercase) if char.isupper() else list(string.ascii_lowercase)
    )
    new_index = (alphabets.index(char) + shift) % 26
    return alphabets[new_index]


def caesar_cipher(secret_code, shift, operation):
    result = []
    if operation == "decrypt":
        shift *= -1
    for char in secret_code:
        if char.isalpha():
            result.append(shift_char(char, shift))
        else:
            result.append(char)
    print("".join(result))


def main():
    subprocess.run("clear", shell=True)
    print("WELCOME TO CAESAR CIPHER")
    print("=" * 25)
    secret_code = input("\nEnter your secret code\n→ ")
    shift = int(input("Enter shift value\n→ "))
    # Validate operation input
    operation = input("What operation do you want to perform [encrypt/decrypt] \n→ ")
    while operation != "encrypt" and operation != "decrypt":
        print("⚠️ Invalid operation. Please try again.")
        operation = input("What operation do you want to perform [encrypt/decrypt]\n→ ")
    caesar_cipher(secret_code, shift, operation)


if __name__ == "__main__":
    main()
