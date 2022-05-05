def main():
    grocery_dict, grocery_list = get_input()
    grocery_list.sort()
    print("\n")
    display_list(grocery_dict, grocery_list)


def get_input(prompt = ""):
    grocery_dict = {}
    grocery_list = []
    while True:
        try:
            item = input(prompt)
            item = item.upper()
            if item == "":
                continue
            elif item not in grocery_dict:
                grocery_dict[item] = 1
                grocery_list.append(item)

            else:
                grocery_dict[item] += 1
        except EOFError:
            break

    return grocery_dict, grocery_list

def display_list(dict1, arr):
    for item in arr:
        print(f"{dict1[item]} {item}")

main()