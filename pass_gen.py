python project
# Project Title:
# Password Generator

# Project Description:
# This project is a Python-based application that generates secure and random passwords based on user-defined criteria. The user can specify the password length and choose which types of characters to include, such as uppercase letters, lowercase letters, numbers, and special symbols.

# Working of the Project:
# User Input
# The program asks the user:
# Password length
# Whether to include uppercase letters, lowercase letters, digits, and symbols
# Character Pool Creation
# Based on user choices, the program creates a pool of characters using:
# Letters (A-Z, a-z)
# Numbers (0-9)
# Special characters (!@#$...)
# Password Generation
# At least one character from each selected category is added
# Remaining characters are filled randomly from the pool
# The final password is shuffled to ensure randomness
# Output
# A secure, randomly generated password is displayed

# Technologies Used:
# Python
# Built-in modules: random, string


import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length <= 0:
        return "Error: Length must be greater than 0"

    characters = ""
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if use_lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        return "Error: Select at least one character type"

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
    except:
        print("Invalid input. Enter a number.")
        return

    use_upper = input("Include uppercase (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase (y/n): ").lower() == 'y'
    use_digits = input("Include digits (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    print("\nGenerated Password:", password)


if __name__ == "__main__":
    main()
