def data_type(type, number):
    if type == "int":
        print(int(number) * 2)
    elif type == "real":
        print(f"{(float(number) * 1.5):.2f}")
    elif type == "string":
        print(f"${number}$")


type_data = input()
num = input()
data_type(type_data, num)
