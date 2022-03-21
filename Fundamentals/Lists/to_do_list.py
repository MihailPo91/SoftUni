chore = input()
todo = ["" for i in range(11)]


while chore != "End":
    current = chore.split("-")[1]
    index = int(chore.split("-")[0])
    todo[index] = current

    chore = input()

final_list = [ch for ch in todo if ch != ""]
print(final_list)
