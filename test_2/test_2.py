def main():
    while True:
        try:
            fraction = get_input("Fraction:")
            percentage = convert(fraction)
            print(gauge(percentage))
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

def convert(fraction):
    x = fraction[:fraction.index("/")]
    y = fraction[fraction.index("/") + 1:]
    if int(y) == 0:
        raise ZeroDivisionError
    if (int(y) < int(x)):
        raise ValueError

    x = int(x)
    y = int(y)

    fraction = x/y

    return int(fraction * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def get_input(prompt):
    inputt = input(prompt)
    return inputt

if __name__ == "__main__":
    main()
