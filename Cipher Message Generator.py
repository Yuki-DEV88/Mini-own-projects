import random
import string

menu = {1 : "generate an encrypt message",
        2 : "decrypt a message",
        3 : "exit"}

def header():
    print("=======================================")
    print("         CIPHER TEXT GENERATOR         ")
    print("          (ENCODE AND DECODE)          ")
    print("=======================================")

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

def main():
    while True:
        header()
        for key, value in menu.items():
            print(f"{key}. {value}")
        print("=======================================")
        action = input("What do you want to do?: ").lower()
        print("=======================================")
        match action:
            case "1" | "generate an encrypt message":
                while True:
                    encrypt = input("Enter a message to encrypt (:q to quit): ")
                    encrpt = ""

                    if encrypt not in (":q", ":quit"):
                        for letter in encrypt:
                            if letter in chars:
                                index = chars.index(letter)
                                encrpt += keys[index]
                            else:
                                encrpt += letter
                        print("=======================================")
                        print(f"YOUR ENCRYPTED MESSAGE IS: {encrpt}")
                        print("=======================================")
                    else:
                        break
                continue
            case "2" | "decrypt a message":
                while True:
                    decrypt = input("Enter a message to decrypt (:q to :quit): ")
                    dcrpt = ""

                    if decrypt not in (":q", ":quit"):
                        for letter in decrypt:
                            if letter in keys:
                                index = keys.index(letter)
                                dcrpt += chars[index]
                            else:
                                dcrpt += letter
                        print("=======================================")
                        print(f"THE DECRYPTED MESSAGE IS: {dcrpt}")
                        print("=======================================")
                    else:
                        break
                continue
            case "3" | "exit":
                print("         THANK YOU FOR VISITING!       ")
                print("=======================================")
                break

if __name__ == "__main__":
    main()