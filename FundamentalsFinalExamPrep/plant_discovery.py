number = int(input())
plant_dict = {}

for line in range(number):
    data = input().split("<->")
    plant = data[0]
    rarity = data[1]
    if plant not in plant_dict:
        plant_dict[plant] = {}
        plant_dict[plant]["rarity"] = int(rarity)
    elif plant in plant_dict:
        plant_dict[plant]["rarity"] = int(rarity)

while True:
    line = input()
    if line == "Exhibition":
        break
    else:
        data = line.split(": ")
        command = data[0]
        if command == "Rate":
            misc = data[1].split(" - ")
            plant = misc[0]
            rating = int(misc[1])
            if plant in plant_dict:
                if "rating" in plant_dict[plant]:
                    plant_dict[plant]["rating"].append(rating)
                else:
                    plant_dict[plant]["rating"] = []
                    plant_dict[plant]["rating"].append(rating)
            else:
                print("error")
        elif command == "Update":
            misc = data[1].split(" - ")
            plant = misc[0]
            rarity = int(misc[1])
            if plant in plant_dict:
                plant_dict[plant]["rarity"] = int(rarity)
            else:
                print("error")
        elif command == "Reset":
            plant = data[1]
            if plant in plant_dict:
                plant_dict[plant]["rating"] = []
            else:
                print("error")

for k, v in plant_dict.items():
    if not plant_dict[k]['rating']:
        plant_dict[k]['rating'] = 0
    else:
        plant_dict[k]['rating'] = sum(plant_dict[k]['rating']) / len(plant_dict[k]['rating'])

print("Plants for the exhibition:")
for key in plant_dict:
    print(f"- {key}; Rarity: {plant_dict[key]['rarity']}; Rating: {plant_dict[key]['rating']:.2f}")
