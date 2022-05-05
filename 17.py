def main():
    time = input("what time is it right now?")
    time = time.replace(" ", "")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hour = time[:time.index(":")]
    return int(hour)


if __name__ == "__main__":
    main()
