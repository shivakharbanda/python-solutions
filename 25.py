string = input("Input:")
size = len(string)

string = list(string)

for i in range(size):
    if "a" in string:
        string.remove("a")
    elif "A" in string:
        string.remove("A")
    elif "e" in string:
        string.remove("e")
    elif "E" in string:
        string.remove("E")
    elif "i" in string:
        string.remove("i")
    elif "I" in string:
        string.remove("I")
    elif "o" in string:
        string.remove("o")
    elif "O" in string:
        string.remove("O")
    elif "u" in string:
        string.remove("u")
    elif "U" in string:
        string.remove("U")

print("".join(string))