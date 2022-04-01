number = int(input())
music_box = {}

for item in range(number):
    piece, composer, key = input().split("|")
    if piece not in music_box:
        music_box[piece] = {}
        music_box[piece]["composer"] = composer
        music_box[piece]["key"] = key

while True:
    line = input()
    if line == "Stop":
        break
    else:
        data = line.split("|")
        command = data[0]
        if command == "Add":
            piece = data[1]
            composer = data[2]
            key = data[3]
            if piece not in music_box.keys():
                music_box[piece] = {}
                music_box[piece]["composer"] = composer
                music_box[piece]["key"] = key
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")
        elif command == "Remove":
            piece = data[1]
            if piece in music_box.keys():
                music_box.pop(piece)
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        elif command == "ChangeKey":
            piece = data[1]
            new_key = data[2]
            if piece in music_box.keys():
                music_box[piece]["key"] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")

for key in music_box:
    print(f"{key} -> Composer: {music_box[key]['composer']}, Key: {music_box[key]['key']}")
