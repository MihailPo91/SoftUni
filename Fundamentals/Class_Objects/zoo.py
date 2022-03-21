class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        animal = name

        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fish.append(animal)
        elif species == "bird":
            self.birds.append(animal)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        if species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fish)}\n"
        if species == "bird":
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
