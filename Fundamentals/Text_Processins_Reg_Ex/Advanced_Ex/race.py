import re

participants = input().split(", ")
scores = {}

while True:
    line = input()
    if line == "end of race":
        break
    else:
        word_pattern = r"[A-Za-z]+"
        name = ''.join(re.findall(word_pattern, line))
        num_pattern = r"\d"
        distance = sum(map(int, [num for num in re.findall(num_pattern, line)]))
        if name in participants:
            if name not in scores:
                scores[name] = distance
            else:
                scores[name] += distance

sorted_scores = sorted(scores, key=scores.get, reverse=True)
print(f"1st place: {sorted_scores[0]}")
print(f"2nd place: {sorted_scores[1]}")
print(f"3rd place: {sorted_scores[2]}")

