def header():
    print("-----GROCERY CART CALCULATOR-----")

header()

items = []
prices = []
quantities = []
total = 0

def body():
    global item
    while True:
        try:
            item = input("What item did you bought? (e for exit): ")
            if item != "e":
                main()
            else:
                break
        except ValueError:
            print("TRY AGAIN!")


def main():
        items.append(item)
        while True:
            try:
                price = float(input("Enter the price of that item: "))
                prices.append(price)
                break
            except ValueError:
                print("PRICES MUST BE NUMBER ONLY!") 
        while True:
            try:   
                quantity = float(input("How many did you bought?: "))
                quantities.append(quantity)
                break
            except ValueError:
                print("QUANTITY MUST BE IN VALUE ONLY!")

def cart():
    print("----------YOUR CART TOTAL---------")
    for item, price, quantity in zip(items, prices, quantities):
        print(f"{item:5} ${price:5} x{quantity:5}")
        subtotal = price * quantity
        global total
        total += subtotal
    
    print("----------------------------------")
    print(f"YOUR TOTAL COST IS: ${total:.2f}")
    print("----------------------------------")

body()
        
cart()

while True:
    ask = input("Calculate again? (y/n): ")
    if ask not in ("y", "n"):
        print("INVALID CHOICE!")
    elif ask == "n":
        print("THANK YOU! SEE YOU AGAIN!")
        break
    else:
        if ask == "y":
            items.clear()
            prices.clear()
            quantities.clear()
            total = 0
        
        header()
        body()
        cart()