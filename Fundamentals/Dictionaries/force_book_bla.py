items = input()
users = {}
while items != "Lumpawaroo":
    if "|" in items:
        tokens = items.split(" | ")
        side = tokens[0]
        user = tokens[1]
        check = False
        for key, values in users.items():
            if user in values:
                check = True
                break
        if check is False:
            if side not in users:
                users[side] = [user]
            elif side in users and user not in users[side]:
                users[side].append(user)
    elif "->" in items:
        tokens = items.split(" -> ")
        user = tokens[0]
        side = tokens[1]
        for key, values in users.items():
            if user in values:
                values.remove(user)
                break
        if side not in users:
            users[side] = [user]
            print(f"{user} joins the {side} side!")
        elif side in users and user not in users[side]:
            users[side].append(user)
            print(f"{user} joins the {side} side!")
    items = input()

for key, values in users.items():
    if len(values) > 0:
        print(f"Side: {key}, Members: {len(values)}")
        for v in values:
            print(f"! {v}")