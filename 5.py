coke_cost = 50
while coke_cost != 0:
    print(f"Amout Due: {coke_cost}")

    coin = input("Insert Coin:")
    coin = int(coin)
    change = 0

    if (coin == 25 or coin == 10 or coin == 5) and coin <= coke_cost:
        coke_cost -= coin

    if coke_cost == 0:
        print(f"Change Owned: {coke_cost}")
        break

    if coin > coke_cost:
        print("that")
        change = coin - coke_cost
        print(f"Change Owned: {change}")
        break
