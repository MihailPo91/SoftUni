first_player = int(input())
second_player = int(input())

while first_player != 0 and second_player != 0:
    command = input()

    if command == "End of battle":
        break

    elif command == "one":
        second_player -= 1

    elif command == "two":
        first_player -= 1

if first_player == 0:
    print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
elif second_player == 0:
    print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
else:
    print(f"Player one has {first_player} eggs left.")
    print(f"Player two has {second_player} eggs left.")
