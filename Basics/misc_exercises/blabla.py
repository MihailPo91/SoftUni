temperature = int(input("What's the temperature today? "))
if temperature > 30:
    print("It's hot!")
    print("Drink more water!")
elif temperature >= 15:
    print("It's nice!")
    print("Great weather for a walk!")
elif temperature <= 14:
    print("It's cold!")
    print("Wear warm clothes today.")
else:
    print("You should type a valid temperature value! Try again.")