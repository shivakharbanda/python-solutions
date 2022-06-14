def main():
    plate = input("Plate: ")


    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) >= 2 and len(s) <= 6 and check_invalid_chars(s):

        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        letters = ['a', 'b', 'C', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if s[0] in numbers:
            return False

        number_part = ""

        for i in range(len(s)):
            #print("s[i]:", s[i], s[i] in numbers)
            if s[i] in numbers:
                letter_part = s[:i]
                number_part = s[i:]
                break

    else:
        return False

    if number_part == "":
        return True

    return check_num(number_part)


def check_invalid_chars(s):

    invalid_chars = [".", " ", ",", ":", "_", "-", ";"]
    #print("s", s, "invalid", invalid_chars)
    for i in range(len(s)):
        #print("s[i]:", s[i], "s[i] in invalid_chars", s[i] in invalid_chars)
        if s[i] in invalid_chars:
            return False
    return True

def check_num(n):
    #print("n:", n)
    if n[0] == "0":
        return False
    else:
        letters = ['a', 'b', 'C', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
       
        if n[-1].lower() in letters:
            return False

        for i in range(len(n)):
            if n[i] in letters:
                return False

        return True



if __name__ == "__main__":
    main()
