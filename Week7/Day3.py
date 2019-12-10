import string
from random import choice, shuffle

special_char = '!@#$%^&*_~'
full_pool = string.ascii_letters + string.digits + special_char

def create_password(length):
    password = []
    password.append(choice(string.digits))
    password.append(choice(string.ascii_lowercase))
    password.append(choice(string.ascii_uppercase))
    password.append(choice(special_char))
    while len(password) < length:
        password.append(choice(full_pool))

    shuffle(password)
    return ''.join(password)

def main():
    length = input("How many characters would you like in your password: ")
    try:
        length = int(length)
    except ValueError:
        print("Sorry, invalid input. Must be a number")
        return

    if not 6 <= length <= 30:
        print("Invalid length. Password must be between 6-30 characters.")
        return
    print(f"Here is your randomly generated password: {create_password(length)}")
    print("Write it down somewhere safe.")


main()