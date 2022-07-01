import random
#random module to generate random numbers
import string 
#string module to create a random string


print("Welcome to Random Password Generator :)")
characters = string.ascii_letters + string.digits + string.punctuation
passwords = int(input("Enter the number of passwords you want to generate: "))
#generates n no.of passwords according to user input
length = int(input("Enter your password length: "))
#password length

print("Your passwords:")

for pwd in range(passwords):
    password = ''
    for i in range (length):
        password += random.choice(characters)
    print(password)
