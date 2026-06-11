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
        print("THANK YOU FOR PLAYING!")
        break