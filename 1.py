import inflect

p = inflect.engine()

names = []
while True:
    try:
        string = input("Input:")
        names.append(string)
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names)}")