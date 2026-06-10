foods = {"pizza" : 95.75,
         "soda" : 35.00,
         "lemonade" : 79.99,
         "chips" : 25.00,
         "buko juice" : 85.65,
         "nachos" : 33.67,
         "fries" : 50.20,
         "bottled water" : 20.00,
         "hotdog" : 25.25}

cart = {}
total = 0

print("*******************************")
print("    YUKI'S CONCESSION STAND    ")
print("*******************************")
print("            WELCOME!           ")
print("        HERE IS OUR MENU!      ")
print("-------------------------------")
print("              MENU             ")
print("-------------------------------")

for key, value in foods.items():
    print(f"{key:<15}   :    ₱{value:>7}")
print("-------------------------------")

while True:
    order = input("What is your order? ('q' to quit):  ").lower()
    if order == "q":
        break
    elif foods.get(order) is not None:
        quantity = int(input("How many?: "))
        cart[order] = cart.get(order, 0) + quantity
    else:
        print("Sorry we dont have that order.")

print("*******************************")
print("    ~~~~~~ YOUR CART ~~~~~     ")
print("-------------------------------")

for food, quantity in cart.items():
    price = foods.get(food)
    subtotal = price * quantity
    total += subtotal
    print(f"{food:<10}x{quantity}  : ₱{price} = ₱{subtotal:.2f}")
print("-------------------------------")
print(f"YOUR TOTAL COST IS: ₱{total:.2f}")
print("=================================")
print("        PLEASE BUY AGAIN!        ")
print("=================================")