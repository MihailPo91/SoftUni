inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_found = False

while not is_found:
    farm = input().split(" ")
    for i in range(0, len(farm), 2):
        item = farm[i + 1].lower()
        quantity = int(farm[i])

        if item in inventory:
            inventory[item.lower()] += quantity
            if item == "shards":
                if inventory["shards"] >= 250:
                    print("Shadowmourne obtained!")
                    is_found = True
                    inventory["shards"] -= 250
                    break
            elif item == "fragments":
                if inventory["fragments"] >= 250:
                    print("Valanyr obtained!")
                    is_found = True
                    inventory["fragments"] -= 250
                    break
            elif item == "motes":
                if inventory["motes"] >= 250:
                    print("Dragonwrath obtained!")
                    is_found = True
                    inventory["motes"] -= 250
                    break
        else:
            if item not in junk:
                junk[item] = quantity
            else:
                junk[item] += quantity
    if is_found:
        break

print(f"shards: {inventory['shards']}")
print(f"fragments: {inventory['fragments']}")
print(f"motes: {inventory['motes']}")
for key in junk:
    print(f"{key.lower()}: {junk[key]}")
