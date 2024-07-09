import random
import string

def password_generator():
    password_length = int(input("Enter the desired length of the password: "))
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(password_length))
    print("Generated Password : ", password)

password_generator()
