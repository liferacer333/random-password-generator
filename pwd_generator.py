import random
#random module to generate random numbers
import string 
#string module to create a random string
print("""
	####################################################################
	#      PYTHON - Random Password Generetor (RPG) - Liferacer333     #
	####################################################################
	#                         CONTACT                                  #
	####################################################################
	#               DEVELOPER : Hemanth Reddy                          #
	#          Mail Address : hemanth.reddy2547@gmail.com              #
	#  LINKEDIN : https://www.linkedin.com/in/hemanth-reddy-51b357191/ #
	#                                                                  #
	####################################################################
""")

print("Welcome to Random Password Generator :)")
characters = string.ascii_letters + string.digits + string.punctuation
passwords = int(input("Enter the number of passwords you want to generate: "))
#generates n no.of passwords according to user input

length = int(input("Enter your password length: "))
#password length

file = "passwords.txt"
#passwords are saved in the passwords.txt file

print("Your passwords are saved in the",file, "file")
sys.stdout = open(file, "w")
print("Your passwords: \n")
print("Your passwords:")

for pwd in range(passwords):
    password = ''
    for i in range (length):
        password += random.choice(characters)
    print(password)
