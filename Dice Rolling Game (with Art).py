import random

art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│       ● │",
        "│    ●    │",
        "│ ●       │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}

while True:
    print("===========================")
    print("   ~ DICE ROLLING GAME ~   ")
    print("===========================")

    total = 0
    dice = []

    num = int(input("How many dice?: "))

    for die in range(num):
        dice.append(random.randint(1, 6))

    for line in range(5):
        for die in dice:
            print(art.get(die)[line], end= " ")
        print()

    for die in dice:
        total += die
    print("=====================")
    print(f"TOTAL SCORE: {total}")
    print("=====================")

    while True:
        ask = input("Continue?: ")
        if ask not in ("y", "n"):
            print("INVALID INPUT!")
        else:
            break
        
    if ask == "y":
        dice.clear()
        continue
    else:
        print("============================")
        print(" ~ THANK YOU FOR PLAYING! ~ ")
        print("============================")
        break