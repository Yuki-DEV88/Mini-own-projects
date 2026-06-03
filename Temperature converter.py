# Menu function
def menu():
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Celcius to kelvin")
    print("4. Kelvin to Celcius")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to kelvin")

while True:
    try:
    # The Main menu
        print("*****TEMPERATURE CONVERTER*****")
        menu()
        print("*******************************")
    # Input of conversions and values
        question = input("What do you want to convert?: ").lower()
        value = float(input("Enter a value: "))
    # Formulas
        if question in ("1", "celcius to fahrenheit"):
            result = (value * 9/5) + 32
            output_unit = "°F"
        elif question in ("2", "fahrenheit to celcius"):
            result = (value - 32) * 5/9
            output_unit = "°C"
        elif question in ("3", "celcius to kelvin"):
            result = value + 273.15
            output_unit = "K"
        elif question in ("4", "kelvin to celcius"):
            result = value - 273.15
            output_unit = "°C"
        elif question in ("5", "kelvin to fahrenheit"):
            result = (value - 273.15) * 9/5 + 32
            output_unit = "°F"
        elif question in ("6", "fahrenheit to kelvin"):
            result = (value - 32) * 5/9 + 273.15
            output_unit = "K"
    # In case user typed something wrong
        else:
            print("CONVERSION NOT FOUND.")
            continue
    # In case user input a letter rather than a number
    except ValueError:
        print("PLEASE TRY AGAIN!")
        continue
    # Display of Result
    print("*****RESULT*****")
    print(f"The result is: {result:.2f}{output_unit}")
    print("----------------")
    # Ask for continuation
    ask = input("Would you like to continue?: ").lower()
    if ask not in ("y", "yes"):
        print("Thank you for visiting!")
        break