count = int(input())
parking_lot = set()

for car in range(count):
    direction, license_plate = input().split(', ')
    if direction == 'IN':
        parking_lot.add(license_plate)
    elif direction == 'OUT' and license_plate in parking_lot:
        parking_lot.remove(license_plate)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print('Parking Lot is Empty')
