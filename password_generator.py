import string
import random


def pword_gen():
    password_char = string.ascii_letters + string.punctuation + string.digits
    length = int(input("Enter the length of the password: "))
    password = ""
    for i in range(0, length):
        password = password + random.choice(password_char)
    print(password)


pword_gen()
