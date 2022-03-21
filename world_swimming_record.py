swimming_record = float(input())
distance = float(input())
time_for_meter = float(input())
resistance = (distance // 15) * 12.5
total_time = distance * time_for_meter + resistance
diff = abs(swimming_record - total_time)
if swimming_record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")