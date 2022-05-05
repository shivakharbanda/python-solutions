inputt = input("Greeting:")

inputt = inputt.lower()
inputt = inputt.strip()

if inputt[:5] == "hello":
    print("$0")
elif inputt[:5] != "hello" and inputt[0] == "h":
    print("$20")

else:
    print("$100")