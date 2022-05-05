def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    Total = 0
    while True:
        try:
            item = input("Item:").title()
            Total = float(Total)
            if item in menu:
                Total += menu[item]
        except (EOFError):
            print("\n")
            break
        except KeyError:
            pass

        Total ="%.2f" % Total
        print(f"Total: ${Total}")


main()