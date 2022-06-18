from collections import deque

elves_queue = deque([int(x) for x in input().split()])
material_boxes_stack = [int(x) for x in input().split()]
toys = 0
energy_used = 0
counter = 1

while True:
    if not material_boxes_stack or not elves_queue:
        break

    current_elf = elves_queue.popleft()
    current_box = material_boxes_stack.pop()

    if current_elf < 5:
        material_boxes_stack.append(current_box)
        counter += 1
        continue

    if counter % 3 == 0:

        if current_elf < current_box * 2:
            material_boxes_stack.append(current_box)
            current_elf *= 2
            elves_queue.append(current_elf)

        elif current_elf >= current_box * 2:
            energy_used += current_box * 2
            current_elf -= current_box * 2
            if counter % 5 == 0:
                elves_queue.append(current_elf)
                counter += 1
                continue
            toys += 2
            current_elf += 1
            elves_queue.append(current_elf)

        counter += 1
        continue

    if current_elf < current_box:
        material_boxes_stack.append(current_box)
        current_elf *= 2
        elves_queue.append(current_elf)

    elif current_elf >= current_box:
        energy_used += current_box
        current_elf -= current_box
        if counter % 5 == 0:
            elves_queue.append(current_elf)
            counter += 1
            continue
        toys += 1
        current_elf += 1
        elves_queue.append(current_elf)
    counter += 1

print(f"Toys: {toys}")
print(f"Energy: {energy_used}")
if elves_queue:
    print(f"Elves left: {', '.join([str(x) for x in elves_queue])}")
if material_boxes_stack:
    print(f"Boxes left: {', '.join([str(x) for x in material_boxes_stack])}")