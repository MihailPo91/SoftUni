import re
attacked_planets = {'attacked': [], 'destroyed': []}
validation_pattern = r"@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+)"

n = int(input())
for i in range(n):
    message = input()
    count_key_letters = len(re.findall(r"[s,t,a,r,S,T,A,R]", message))
    if count_key_letters == 0:
        pass
    new_message = ""
    for lt in message:
        new_message += chr(ord(lt)-count_key_letters)

    planet = ''.join(re.findall(r"[@]([A-Za-z]+)", new_message))
    population = ''.join(re.findall(r"[:](\d+)", new_message))
    attack_type = ''.join(re.findall(r"[!]([A|D])[!]", new_message))
    soldier_count = ''.join(re.findall(r"[\->](\d+)", new_message))

    verify = re.findall(validation_pattern, new_message)

    if len(verify) > 0:
        if attack_type == "A":
            attacked_planets['attacked'].append(planet)
        elif attack_type == "D":
            attacked_planets['destroyed'].append(planet)

print(f"Attacked planets: {len(attacked_planets['attacked'])}")
for key in sorted(attacked_planets['attacked']):
    print(f"-> {key}")
print(f"Destroyed planets: {len(attacked_planets['destroyed'])}")
for key in sorted(attacked_planets['destroyed']):
    print(f"-> {key}")



