number_of_heroes = int(input())

heroes = {}

for char in range(number_of_heroes):
    hero, hp, mp = input().split(" ")
    heroes[hero] = {"health": int(hp), "mana": int(mp)}

while True:
    line = input()
    if line == "End":
        break

    explode = line.split(" - ")
    command = explode[0]

    if command == "CastSpell":
        hero = explode[1]
        mana_needed = int(explode[2])
        spell = explode[3]
        if heroes[hero]["mana"] >= mana_needed:
            heroes[hero]["mana"] -= mana_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mana']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command == "TakeDamage":
        hero = explode[1]
        damage = int(explode[2])
        attacker = explode[3]
        heroes[hero]["health"] -= damage
        if heroes[hero]["health"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['health']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif command == "Recharge":
        hero = explode[1]
        amount = int(explode[2])
        current_mana = heroes[hero]["mana"]
        heroes[hero]["mana"] += amount

        if heroes[hero]["mana"] > 200:
            print(f"{hero} recharged for {abs(200 - current_mana)} MP!")
            heroes[hero]["mana"] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")

    elif command == "Heal":
        hero = explode[1]
        amount = int(explode[2])
        current_health = heroes[hero]["health"]
        heroes[hero]["health"] += amount

        if heroes[hero]['health'] > 100:
            heroes[hero]['health'] = 100
            print(f"{hero} healed for {abs(100 - current_health)} HP!")
        else:
            print(f"{hero} healed for {amount} HP!")

for key, value in heroes.items():
    print(key)
    print(f"  HP: {heroes[key]['health']}")
    print(f"  MP: {heroes[key]['mana']}")

