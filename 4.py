def camel_to_snake(string):
    snake_case = ""
    last_letter_num = 0
    this_letter_num = 0
    x = 0
    for i in range(len(string)):
        if string[i].isupper():
            #print("i:", i, "x:", x, "snake_case:", snake_case)
            snake_case += string[x : i] + "_"
            x = i

    return snake_case + string[x:]

camel_case_input = input("camelCase:")

snake = camel_to_snake(camel_case_input)
print(f"snake_case:{snake.lower()}")
