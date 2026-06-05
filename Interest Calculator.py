def menu():
    print("-----INTEREST CALCULATOR-----")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("-----------------------------")

while True:
    try:
        menu()
        ask = input("What do you want to solve?: ")

        if ask == "1" or ask == "simple interest":
            while True:
                principal = float(input("Enter a Principal: "))
                if principal > 0:
                    break
                print("Prinicipal must not be less than or below zero.")
            while True:
                rate = float(input("Enter a Rate (must be in decimal form): "))
                if rate > 0:
                    break
                print("Rate must not be less than or below zero.")
            while True:
                time = float(input("Enter Time: "))
                if time > 0:
                    break
                print("Time must not be less than or below zero.")
            formula = principal * rate * time
            print("-----RESULT-----")
            print(f"The Interest is: {formula:,.2f}")
            total_amount = principal + formula
            print(f"Total ammount with interest: {total_amount:,.2f} ")
            print("----------------------------------------------")
            again = input("Solve again?: ")
            if again not in ("y", "yes"):
                print("Thank you for using us!")
                break
        elif ask == "2" or ask == "compound interest":
            while True:
                principal = float(input("Enter a Principal: "))
                if principal > 0:
                    break
                print("Prinicipal must not be less than or below zero.")
            while True:
                rate = float(input("Enter a Rate (must be in decimal form): "))
                if rate > 0:
                    break
                print("Rate must not be less than or below zero.")
            while True:
                time = float(input("Enter Time: "))
                if time > 0:
                    break
                print("Time must not be less than or below zero.")
            while True:
                n = float(input("Enter Frequency: "))
                if n > 0:
                    break
                print("Frequency must not be less than or below zero.")
            formula = principal * (1 + rate / n) ** (n * time)
            print("-----RESULT-----")
            print(f"The Total Accumulation amount is: {formula:,.2f}")
            print("---------------------------------------------------")
            again = input("Solve again?: ")
            if again not in ("y", "yes"):
                print("Thank you for using us!")
                break
        else:
            print("INVALID CHOICE!")
    except ValueError:
        print("INPUT MISMATCH. PLEASE TRY AGAIN!")