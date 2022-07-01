class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result_string = f"Name: {self.name}\n"
        result_string += f"Guild: {self.guild}\n"
        result_string += f"HP: {self.hp}\n"
        result_string += f"MP: {self.mp}\n"
        for skill in self.skills:
            result_string += f"==={skill} - {self.skills[skill]}\n"
        return result_string

