expresion = input("Expresion:")
expresion = expresion.replace(" ", "")

if expresion.find("+") != -1:
    ind = expresion.index("+")
    print(int(expresion[:ind]) + int(expresion[ind + 1:]) + 0.0)

elif expresion.find("-") != -1:
    ind = expresion.index("-")
    print(int(expresion[:ind]) - int(expresion[ind + 1:])+ 0.0)

elif expresion.find("*")!= -1:
    ind = expresion.index("*")
    print(int(expresion[:ind]) * int(expresion[ind + 1:])+ 0.0)

elif expresion.find("/")!= -1:
    ind = expresion.index("/")
    print(int(expresion[:ind]) / int(expresion[ind + 1:])+ 0.0)
