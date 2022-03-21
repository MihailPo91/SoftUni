force_book = {}
unique_users = set()

while True:
    new_line = input()

    if new_line == "Lumpawaroo":
        break

    elif "|" in new_line:
        line_listed = new_line.split(" | ")
        force_side = line_listed[0]
        user = line_listed[1]
        check = False
        for key, values in force_book.items():
            if user in values:
                check = True
                break
        if check is False:
            if force_side not in force_book:
                force_book[force_side] = [user]
            elif force_side in force_book and user not in force_book[force_side]:
                force_book[force_side].append(user)

    elif "->" in new_line:
        line_listed = new_line.split(" -> ")
        user = line_listed[0]
        force_side = line_listed[1]
        for key, values in force_book.items():
            if user in values:
                values.remove(user)
                break
        if force_side not in force_book:
            force_book[force_side] = [user]
            print(f"{user} joins the {force_side} side!")
        elif force_side in force_book and user not in force_book[force_side]:
            force_book[force_side].append(user)
            print(f"{user} joins the {force_side} side!")

for key, values in force_book.items():
    if len(values) > 0:
        print(f"Side: {key}, Members: {len(values)}")
        for v in values:
            print(f"! {v}")