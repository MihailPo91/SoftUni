pirate_map = {}

while True:
    line = input()
    if line == "Sail":
        break
    else:
        data = line.split('||')
        city = data[0]
        population = int(data[1])
        gold = int(data[2])
        if city not in pirate_map.keys():
            pirate_map[city] = {"population": population, "gold": gold}
        else:
            pirate_map[city]["population"] += population
            pirate_map[city]["gold"] += gold

while True:
    line = input()
    if line == "End":
        break
    else:
        data = line.split('=>')
        command = data[0]
        if command == "Plunder":
            town = data[1]
            people = int(data[2])
            gold = int(data[3])
            current_population = pirate_map[town]["population"]
            current_gold = pirate_map[town]["gold"]
            pirate_map[town]["population"] -= people
            pirate_map[town]["gold"] -= gold
            if pirate_map[town]["population"] <= 0 and pirate_map[town]["gold"] <= 0:
                print(f"{town} plundered! {current_gold} gold stolen, {current_population} citizens killed.")
                del pirate_map[town]
                print(f"{town} has been wiped off the map!")
            elif pirate_map[town]["population"] <= 0 and pirate_map[town]["gold"] > 0:
                print(f"{town} plundered! {gold} gold stolen, {current_population} citizens killed.")
                del pirate_map[town]
                print(f"{town} has been wiped off the map!")
            elif pirate_map[town]["population"] > 0 and pirate_map[town]["gold"] <= 0:
                print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")
                del pirate_map[town]
                print(f"{town} has been wiped off the map!")
            else:
                print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        elif command == "Prosper":
            town = data[1]
            gold = int(data[2])
            if gold >= 0:
                pirate_map[town]["gold"] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {pirate_map[town]['gold']} gold.")
            else:
                print("Gold added cannot be a negative number!")

if len(pirate_map) > 0:
    print(f"Ahoy, Captain! There are {len(pirate_map)} wealthy settlements to go to:")
    for key in pirate_map:
        print(f"{key} -> Population: {pirate_map[key]['population']} citizens, Gold: {pirate_map[key]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
