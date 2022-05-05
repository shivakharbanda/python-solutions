def main():
    while True:

        try:
            fraction = get_input("Fraction:")
            x = fraction[:fraction.index("/")]
            y = fraction[fraction.index("/") + 1:]

            if (int(y) < int(x)):
                raise ValueError("Bag thing happend")



            x = int(x)
            y = int(y)

            fraction = x/y

            percentage = fuel_percentage(fraction)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

        else:
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

def fuel_percentage(x):
    percentage = (x) * 100
    return int(percentage)

def get_input(prompt):
    inputt = input(prompt)
    return inputt

print(main())