import time

def menu():
    print("~~~~~~~~~~COUNTDOWN TIMER~~~~~~~~~~")
    print('~"Reminding you your time of you~"~')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def countdown():
    timer = int(input("Set your timer: "))
    reminder = input("Set reminder: ")
    print("~~~~~~~~~~~STARTING~~~~~~~~~~~~")
    for i in range(timer, 0, -1):
        seconds = i % 60
        minutes = int(i / 60) % 60
        hours = int(i / 3000)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print(f"{reminder}!")

while True:
    try:
        menu()
        countdown()
        while True:
            ask = input("Set timer again? (y/n): ").lower()
            if ask == "y":
                menu()
                countdown()
            elif ask == "n":
                print("Have a great day!")
                break
            else:
                print("INVALID INPUT!")
        break
    except ValueError:
        print("ENTER A PROPER TIME!")
            