import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generator():
    print("Welcome to password generator.")

    check = True
    while check:
        letters_amount = int(input("How many letters would you like in your password?"))
        if letters_amount < 0:
            letters_amount = (input("Wrong number. Please choose how many letters would you like in your password."))
        elif letters_amount == 0:
            confirm = input("Are you sure? Your password might not be strong enough.\n"
                  "Type 'Y' if you are sure you don't want any letters "
                  "or any other button if you would like to add some")
            if confirm in ['Y', 'y']:
                check = False
            else:
                letters_amount = int(input("How many letters would you like in your password?"))
                if letters_amount == 0:
                    print("Are you sure?")
                    continue
                else:
                    check = False
        else:
            check = False
            print(letters_amount)

    check = True
    while check:
        symbols_amount = int(input("How many symbols would you like in your password?"))
        if symbols_amount < 0:
            symbols_amount = (input("Wrong number. Please choose how many symbols would you like in your password."))
        elif symbols_amount == 0:
            confirm = input("Are you sure? Your password might not be strong enough.\n"
                  "Type 'Y' if you are sure you don't want any symbols "
                  "or any other button if you would like to add some")
            if confirm in ['Y', 'y']:
                check = False
            else:
                symbols_amount = int(input("How many symbols would you like in your password?"))
                if symbols_amount == 0:
                    print("Are you sure?")
                    continue
                else:
                    check = False
        else:
            check = False
            print(symbols_amount)

    check = True
    while check:
        numbers_amount = int(input("How many numbers would you like in your password?"))
        if numbers_amount < 0:
            numbers_amount = (input("Wrong number. Please choose how many numbers would you like in your password."))
        elif numbers_amount == 0:
            confirm = input("Are you sure? Your password might not be strong enough.\n"
                  "Type 'Y' if you are sure you don't want any numbers "
                  "or any other button if you would like to add some")
            if confirm in ['Y', 'y']:
                check = False
            else:
                numbers_amount = int(input("How many numbers would you like in your password?"))
                if numbers_amount == 0:
                    print("Are you sure?")
                    continue
                else:
                    check = False
        else:
            check = False
            print(numbers_amount)

    password_list = []

    for letter in range(letters_amount):
        letter = random.choice(letters)
        password_list.append(letter)

    for symbol in range(symbols_amount):
        symbol = random.choice(symbols)
        password_list.append(symbol)

    for number in range(numbers_amount):
        number = random.choice(numbers)
        password_list.append(number)

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    print(f"You password is: {password}")


if __name__ == '__main__':
    generator()

