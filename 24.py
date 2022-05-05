def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    dollars = float(dollars)


    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = str(d)
    return d[1:]

def percent_to_float(p):
    p = str(p)
    p = p[0:len(p) - 1]
    p = int(p)
    p = p / 100
    return p


main()
