import time

points = []

items = ("1. What is the shortcut for 'redo' in computer?: ",
             "2. How many zeros are there in a million? ",
             "3. What is called to an animal who only eat meat: ",
             "4. What do you call a group of fish?: ",
             "5. How many seconds are there on 1 hour?: ")

options = (("A. Ctrl Z", "B. Ctrl V", "C. Ctrl Y", "D. Ctrl X"),
           ("A. 5", "B. 6", "C. 8", "D. 9"),
           ("A. Omnivore", "B. Herbivore", "C. Carnivore", "D. Phentovore"),
           ("A. School", "B. Pride", "C. Group", "D. Team"),
           ("A. 60", "B. 1200", "C. 2400", "D. 3600"))

while True:
    answers = ["C", "B", "C", "A", "D"]
    guesses = []
    scores = 0
    num = 0
    timer = 5

    print("********************************")
    print("           QUIZ GAME            ")
    print("********************************")
    print("A test for your general knowledge!")
    print("             GOODLUCK!            ")
    print("----------------------------------")

    name = input("Enter a username: ")
    
    for item in items:
        print("********************************")
        print(item)
        for option in options[num]:
            print(option)
        print("(You have 5 seconds to answer.)")

        start_time = time.time()
        guess = input("Enter your Answer: ").upper()
        guesses.append(guess)
        end_time = time.time()

        elapse_time = end_time - start_time

        if guess == answers[num] and elapse_time <= timer:
            scores += 1
            print("YOU GOT THE RIGHT ANSWER!")
        elif elapse_time >= timer:
            print(f"TOO SLOW!!. Be faster next time!")
            print(f"The right answer is: {answers[num]}")
        else:
            print(f"Too bad. The right answer is: {answers[num]}")
        num +=1

    print("********************************")
    print("            RESULT              ")
    print("********************************")
    print("Guess: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    print("Correct answers: ", end="")
    for answer in answers:
        print(answer, end= " ")
    print()
    print("********************************")
    point = int(scores / len(items) * 100)
    points.append((name, point))
    print(f"Your score is: {point}%")
    while True:
        ask = input("Play again? (y/n): ")
        if ask not in ("y", "n"):
            print("INVALID INPUT!")
        else: 
            break
    if ask  == "y":
        continue
    else:
        break
print("********* LEADERBOARD *********")
print(f"{'Rank':<10} {'Username':<14} {'Score':<10}")
print("-------------------------------")

points.sort(key=lambda x: x[1], reverse = True)
for rank, entry in enumerate(points, start=1):
    username = entry[0]
    final_score = entry[1]

    print(f"{rank:<10} {username:<14} {final_score}%")


