while True:
    try:
        print("----- WEIGHT & MASS CONVERTER-----")

        unit1 = input("Enter an initial unit: ").lower()
        unit2 = input("Enter a resultant unit: ").lower()
        weight = float(input("Enter the value: "))

        if unit1 in ("kg", "kilogram") and unit2 in ("lbs", "pounds"):
            result = weight * 2.2046
            output_unit = "lbs"
        elif unit1 in ("lbs", "pounds") and unit2 in ("kg", "kilogram"):
            result = weight * 0.453
            output_unit = "kg"
        elif unit1 in ("g", "grams") and unit2 in ("oz", "ounce"):
            result = weight * 0.03527
            output_unit = "oz"
        elif unit1 in ("oz", "ounce") and unit2 in ("g", "grams"):
            result = weight * 28.3495
            output_unit = "g"
        elif unit1 in ("lbs", "pounds") and unit2 in ("g", "grams"):
            result = weight * 453.592
            output_unit = "g"
        elif unit1 in ("g", "grams") and unit2 in ("lbs", "pounds"):
            result = weight * 0.0022
            output_unit = "lbs"
        elif unit1 in ("lbs", "pounds") and unit2 in ("oz", "ounce"):
            result = weight * 16
            output_unit = "oz"
        elif unit1 in ("oz", "ounce") and unit2 in ("lbs", "pounds"):
            result = weight * 0.0625
            output_unit = "lbs"
        elif unit1 in ("g", "grams") and unit2 in ("kg", "kilogram"):
            result = weight * 0.001
            output_unit = "kg"
        elif unit1 in ("kg", "kilogram") and unit2 in ("g", "grams"):
            result = weight * 1000
            output_unit = "g"
        elif unit1 in ("g", "grams") and unit2 in ("mg", "milligrams"):
            result = weight * 1000
            output_unit = "mg"
        elif unit1 in ("mg", "milligrams") and unit2 in ("g", "grams"):
            result = weight * 0.001  
            output_unit = "g"
        elif unit1 in ("oz", "ounce") and unit2 in ("kg", "kilogram"):
            result = weight * 0.0283 
            output_unit = "kg"
        elif unit1 in ("kg", "kilogram") and unit2 in ("oz", "ounce"):
            result = weight * 35.274
            output_unit = "oz"
        elif unit1 in ("lbs", "pounds") and unit2 in ("st", "stone"):
            result = weight * 0.0714
            output_unit = "st"
        elif unit1 in ("st", "stone") and unit2 in ("lbs", "pounds"):
            result = weight * 14
            output_unit = "lbs"
        elif unit1 in ("ton") and unit2 in ("lbs", "pounds"):
            result = weight * 2000
            output_unit = "lbs"
        elif unit1 in ("lbs", "pounds") and unit2 in ("ton"):
            result = weight * 0.0005
            output_unit = "ton"
        else:
            print("PLEASE TRY AGAIN.")
            continue
    except ValueError:
        print("INPUT A PROPER NUMBER!")
        continue

    print("-----RESULT-----")
    print(f"The result is {result:.2f}{output_unit}")
    print("----------------")

    ask = input("Continue? (y/n): ")
    if ask != "y":
        print("Thank you for visiting!")
        break