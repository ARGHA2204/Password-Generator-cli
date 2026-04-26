import random
import string

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
    except:
        print("Invalid input. Using default length 8.")
        length = 8

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_symbols)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()