def main():
    ans = value("How you doing?")
    print(f"${ans}")

def value(greeting):

    inputt = greeting

    inputt = inputt.lower()
    inputt = inputt.strip()


    if inputt[:5] == "hello":
        return 0
    elif inputt[:5] != "hello" and inputt[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()