import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

length = int(input("Enter Password Length: "))
if length <= 0:
    print("Password length must be greater than 0")
    exit()

all_chars = letters + numbers + symbols + uppercase

password = ""

for i in range(length):
    password += random.choice(all_chars)

print("Your Password is:", password)
