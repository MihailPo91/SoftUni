box_of_clothes = list(map(int, input().split()))

rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_counter = 1

while box_of_clothes:
    current_piece = box_of_clothes.pop()
    if current_piece <= current_rack_capacity:
        current_rack_capacity -= current_piece
    else:
        current_rack_capacity = rack_capacity
        racks_counter += 1
        if current_piece <= current_rack_capacity:
            current_rack_capacity -= current_piece

print(racks_counter)