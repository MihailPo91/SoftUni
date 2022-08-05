class Player:
    used_names = set()
    MIN_STAMINA = 0
    MAX_STAMINA = 100

    def __init__(self, name: str, age: int, stamina: int = MAX_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not value:
            raise ValueError("Name not valid!")
        if value in self.used_names:
            raise Exception(f"Name {value} is already used!")
        self.used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def __lt__(self, other):
        return self.stamina < other.stamina

    def __le__(self, other):
        return self.stamina <= other.stamina

    def __eq__(self, other):
        return self.stamina == other.stamina
