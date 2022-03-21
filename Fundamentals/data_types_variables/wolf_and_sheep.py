list_animals = []
animals = input().split(", ")
list_animals += animals
sheep_counter = 0


for i, index in enumerate(reversed(list_animals)):
    sheep_counter += 1
    if index == "wolf" and i == 0:
        print("Please go away and stop eating my sheep")
        break

    if index == "wolf":
        print(f"Oi! Sheep number {sheep_counter -1}! You are about to be eaten by a wolf!")

