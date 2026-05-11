import random

print("🔐 Password Generator v2\n")

letters = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

length = int(input("Enter Password Length: "))


if length <= 0:
    print("Password length must be greater than 0")
    exit()


use_symbols = input("Include symbols? (y/n): ").lower()


all_chars = letters + uppercase + numbers


if use_symbols == "y":
    all_chars += symbols

password = ""

for i in range(length):
    password += random.choice(all_chars)

print("\nYour Password is:", password)
