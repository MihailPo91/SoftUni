countries = input().split(", ")
capitals = input().split(", ")

capital_dict = {country: capital for (country, capital) in zip(countries, capitals)}

for key in capital_dict:
    print(f"{key} -> {capital_dict[key]}")
