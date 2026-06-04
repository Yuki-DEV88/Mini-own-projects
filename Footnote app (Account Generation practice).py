import string

def note():
    print("-----------------------NOTE--------------------------:")
    print("1. Password must have a minimum of 8 characters.")
    print("2. Password must have at least one letter.")
    print("3. Password must have at least one number.")
    print("4. Password must have at least one special character.")
    print("------------------------------------------------------")

def menu():
    print("------------------------FOOTNOTE--------------------------")
    print("Welcome to Footnote!")
    print("A space where you can write all your desires and stories.")
    print("----------------------------------------------------------")


menu()
enter = input("Would you like to enter?: ").lower()
if enter not in ("y", "yes"):
    print("Thank you for your short visit.")
    print("Please come again.")
else:
    print("---------------------------------------------------------")
    print("To enter you must first create an account.")
    while True:
        create_acc = input("Do you want to create an account?: ")
        if create_acc not in ("y", "yes"):
            print("Sorry, you need an account to enter.")
            continue
        else:
            print("-----ACCOUNT CREATION-----")
            username = input("Enter a Username: ")
            while True:
                email = input("Enter Email: ")
                required = "@"
                if required not in email:
                    print("Please input a valid email.")
                    continue
                else:
                    note()
                    while True:
                        password = input("Enter Password: ")
                        if len(password) < 8:
                            print("Your password must have a minimum of 8 characters.")
                        elif not any(char.isalpha() for char in password):
                            print("Your password must consist of at least one letter.")
                        elif not any(char.isdigit() for char in password):
                            print("Your password must consist of at least one number.")
                        elif not any(char in string.punctuation for char in password):
                            print("Your password must consist of at least one special character.")
                        else:
                            while True:
                                confirm = input("Please confirm your password: ")
                                if confirm != password:
                                    print("PASSWORD DOES NOT MATCH!")
                                else:
                                    print("~~YOU HAVE SUCCESSFULLY CREATED AN ACCOUNT!~~")
                                    print("-----ACCOUNT-----")
                                    print("WELCOME!")
                                    print(f"Username: {username}")
                                    print(f"Email: {email}")
                                    print(f"Password: {"*" * len(password)}")
                                    print("-----------------")
                                    ask = input("Enter Footnote?: ").lower()
                                    if ask not in ("y", "yes"):
                                        print("Thank you for visiting!")
                                        break
                                    while True:
                                        menu()
                                        write = input("Enter here what you want to write: ")
                                        print("Saved!")
                                        another = input("Continue?: ").lower()
                                        if another not in ("y", "yes"):
                                            print("See you again!")
                                            break
                                    break
                            break
                break                   
        break