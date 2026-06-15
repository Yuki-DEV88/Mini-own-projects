import random

trans = { 1 : "Deposit",
          2 : "Withdraw",
          3 : "show balance",
          4 : "Play",
          5 : "exit"}

def spin_row():
    symbols = ["❤️", "🐸", "🤯", "🐥"]
    return [(random.choice(symbols)) for _ in range(3)]
def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")
def get_payout(row, amount):
    if row[0] == row[1] == row[2]:
        if row[0] == "🤯":
            return amount * 2
        if row[0] == "🐸":
            return amount * 4
        if row[0] == "🐥":
            return amount * 6
        if row[0] == "❤️":
            return amount * 10
    return 0
def deposit(bal):
    depo = input("How much you want to deposit?: ")
    if depo.isdigit():
        depo = int(depo)
        if depo > 0:
            new_bal = bal + int(depo)
            print("================================")
            print(f"₱{depo} DEPOSITED SUCCESSFULLY!")
            print("================================")
            return new_bal
        print("DEPOSIT MUST BE GREATER THAN ZERO")
        return bal
    print("INVALID AMOUNT")
    return bal
def withdraw(bal):
    withd = input("How much do you want to withdraw?: ")
    if withd.isdigit():
        withd = int(withd)
        if withd <= bal:
            new_bal = bal - withd
            print("================================")
            print(f"₱{withd} WITHDRAW SUCCESSFULLY!")
            print("================================")
            return new_bal
        print("INSUFFICIENT FUNDS")
        return bal
    print("INVALID INPUT!")
    return bal
def show_bal(bal):
    print("================================")
    print(f"YOUR CURRENT BALANCE IS: ₱{bal}")
    print("================================")
    
def main():
    balance = 0
    while True:
        print("===============================")
        print("   🪙   B.P. Slot Machine 🪙  ")
        print("===============================")
        for key, value in trans.items():
            print(f"{key}. {value}")
        print("-------------------------------")
        ask = input("What do you want to do?: ")
        match ask:
            case "1" | "deposit":
                balance = deposit(balance)
            case "2" | "withdraw":
                balance = withdraw(balance)
            case "3" | "show balance":
                show_bal(balance)
            case "4" | "play":
                if balance <= 0:
                    print("========================")
                    print("DEPOSIT AN AMOUNT FIRST!")
                    print("========================")
                    continue
                while balance > 0:
                    print(f"Your current balance is: ₱{balance}")
                    amount = input("Enter your bet amount: ")

                    if not amount.isdigit():
                        print("ENTER A VALID INPUT!")
                        continue
                    amount = int(amount)
                    if amount > balance:
                        print("NOT ENOUGH FUNDS!")
                        continue
                    if amount <= 0:
                        print("BET MUST BE GREATER THAN ZERO!")
                        continue

                    balance -= amount

                    row = spin_row()
                    print("Spining...\n")
                    print_row(row)

                    payout = get_payout(row, amount)
                    if payout > 0:
                        print(f"YOU WON ₱{payout}")
                    else:
                        print("YOU LOSE!")
                    
                    balance += payout

                    again = input("Do you want to spin again?: ").lower()
                    if again != "y":
                        print("THANK YOU FOR PLAYING!")
                        break
                
            case "5" | "exit":
                print("-------------------------")
                print("       GAME OVER!    ")
                print(f"   YOUR BALANCE IS ₱{balance}")
                print("-------------------------")
                break

if __name__ == "__main__":
    main()