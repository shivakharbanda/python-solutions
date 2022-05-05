inputt = input("What is the Answer to the Great Question of Life, the Universe and Everything?")

inputt = inputt.upper()
inputt = inputt.replace(" ", "")

if inputt == "42" or inputt == "FORTY-TWO" or inputt == "FORTYTWO":
    print("Yes")

else:
    print("No")