import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"

length = int(input("Enter Password Length: "))

all_chars = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_chars)

print("Your Password is:", password)
