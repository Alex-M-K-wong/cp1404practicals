def main():


    MIN_LENGTH = 8

    password = get_password()

    while len(password) < MIN_LENGTH:
        print(f"Password is too short. It must be at least {MIN_LENGTH} characters.")
        password = get_password()

    print_the_asterisks(password)


def print_the_asterisks(password):
    print("*" * len(password))


def get_password():
    return input("Enter your password: ")


main()