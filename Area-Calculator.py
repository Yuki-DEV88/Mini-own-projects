import math

def menu():
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Trapezoid")
    print("5. Circle")
    print("6. Ellipse")
    print("7. Parallelogram")

def result():
    print("-----RESULT-----")
    print(f"The result is: {area:.2f}cm2")
    print("----------------")

while True:
    try:
        print("-----AREA CALCULATOR-----")
        menu()
        print("-------------------------")
        
        formula = input("What area of a shape you want to solve?: ")
        if formula in ("1", "Rectangle"):
            width = float(input("Enter the width: "))
            length = float(input("Enter the length: "))
            area = width * length
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("2", "Square"):
            side = float(input("Enter side: "))
            area = side ** 2
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("3", "Triangle"):
            height = float(input("Enter the height: "))
            base = float(input("Enter a base: "))
            area = height * base / 2
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("4", "Trapezoid"):
            base1 = float(input("Enter base 1: "))
            base2 = float(input("Enter base 2: "))
            height = float(input("Enter height: "))
            area = ((base1 + base2) / 2) * height
            result()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("5", "Circle"):
            radius = float(input("Enter a radius: "))
            area = math.pi * (radius ** 2)
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("6", "Ellipse"):
            major_radii = float(input("Enter Major Radii: "))
            minor_radii = float(input("Enter Minor Radii: "))
            area = math.pi * major_radii * minor_radii
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("7", "Parallelogram"):
            base = float(input("Enter a Base: "))
            height = float(input("Enter a Height: "))
            area = base * height
            result()
            ask = input("Continue?: ").lower()
            if ask not in ('y', "yes"):
                print("Thank you for visiting!")
                break
        elif formula in ("n", "No"):
            print("Thank you for visiting!")
            break
        else:
            print("INVALID CHOICE!.")
    except ValueError:
        print("----------------")
        print("PLEASE TRY AGAIN.")
        print("----------------")

    