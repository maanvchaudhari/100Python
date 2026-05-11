import subprocess


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
    return "".join(result)


def main():
    subprocess.run("clear", shell=True)
    message = input("Enter your message\n→ ")
    operation = input("Do you want to encrypt or decrypt\n→ ").strip().lower()
    while operation not in ("encrypt", "decrypt"):
        print("⚠️ Invalid operation, choose either 'encrypt' or 'decrypt'")
        operation = input("Do you want to encrypt or decrypt\n→ ").strip().lower()
    while True:
        try:
            shift = int(input("Enter shift value\n→ "))
            break
        except:
            print("⚠️ Invalid shift value, type in a valid integer number")
    result = caesar_cipher(message, operation, shift)
    print(f"\n{operation.capitalize()}ed message is: {result} ")
    play_again = input("\nWant to try another message? [yes/no]\n→ ").strip().lower()
    while play_again not in ("yes", "no"):
        play_again = (
            input("\nWant to try another message? [yes/no]\n→ ").strip().lower()
        )
    if play_again == "yes":
        main()


if __name__ == "__main__":
    main()
