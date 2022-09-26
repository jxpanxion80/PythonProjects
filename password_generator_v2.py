import random

"""Here is the updated and functioning password generator. Adjustments from the previous code is as 
follows.

defining the 'length in the generator method helped with stopping the reproduction of length 
progressed passwords."""


def generator(length):
    password = ""
    while len(password) != length:
        password = password + random.choice(characters)
    return password


characters = "ABCDEFGHIJKLMONOPQRSTUVWXYZabcdefghijklmonpqrstuvwxyz1234567890`~!@#$%^&*()-+='<,>.?/"

while True:
    print("Choose a number between 8 & 24")
    password_length = int(
        input("Enter password length: "))  # The loop provided here captures the intent of the first code.

    if not password_length < 8 and password_length <= 24:
        new = generator(password_length)
        print(new)
        break
    elif password_length > 8:
        print("Password length is too long")
        continue
    else:
        print("Password length is too short")
        continue

"""Refinment of the loop to fix malfunctions permitted a proper testing of the code. I added 'break' and 
'continue' commands for the program to move to the next step until the user complied with the guidance.
Deleted from this code was the amount of passwords requested. """
