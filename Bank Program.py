def balance(balance: float) -> None:
    print("=================================")
    print(f"Your current balance is: {balance:.2f}")
    print("=================================")
def deposit(balance: float) -> float:
    while True:
        try:
            depo = float(input("How much you want to deposit?: "))
            print("=================================")
            print(f"YOU SUCCESSFULLY DEPOSITED ₱{depo:,.2f}")
            print("=================================")
            return balance + depo
        except ValueError:
            print("PLEASE TRY AGAIN!")
def withdraw(balance: float) -> float:
    while True:
        try:
            withd = float(input("How much do you want to withdraw?: "))
            print("=================================")
            print(f"YOU SUCCESSFULLY WITHDRAW ₱{withd:,.2f}")
            print("=================================")
            return balance - withd
        except ValueError:
            print("PLEASE TRY AGAIN!")
def exit_prog():
    print("=================================")
    print("     ~ PLEASE COME AGAIN! ~      ")
    print("=================================")
    return

choices = {"1" : "Show balance",
           "2" : "Deposit",
           "3" : "Withdraw",
           "4" : "Exit"}

total = 0

print("===========================")
print("       BANGKO CENTRAL      ")
print("===========================")
for key, value in choices.items():
    print(f"{key}. {value}")
print("===========================")

while True:
    ask = input("what do you want to do?: ").capitalize()
    match ask:
        case "1" | "show balance":
            total = balance(total)
        case "2"| "deposit":
            total = deposit(total)
        case "3" | "withdraw":
            total = withdraw(total)
        case "4" | "exit":
            total = exit_prog()
            break
        case _:
            print("INVALID INPUT!")