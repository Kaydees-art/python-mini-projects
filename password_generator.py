import random
import string

letters=input("Include letters? (y/n): ")
numbers=input("Include numbers? (y/n): ")
symbols= input("Include symbols? (y/n): ")

all_characters= " "

if letters== "y":
    all_characters+= string.digits
    if symbols == "y":
        all_characters += string.punctuation

        length= input("How long do you want your password to be? ")
        length= int(length)
        password=" "
for i in range(length):
    password += random.choice(all_characters)

    print("Your password is:", password)
    

