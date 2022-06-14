def main():
    word = get_input()

    print(shorten(word))


def shorten(word):
    list_of_vowvels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

    word = list(word)
    size = len(word)
    i = 0

    for letter in word:

        if letter in list_of_vowvels:
            word.remove(letter)

    return ("".join(word))


def get_input():
    word = input("input:")
    return word


if __name__ == "__main__":
    main()