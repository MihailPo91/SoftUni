from project_1.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):

        result_list_to_string = []

        for player in players:
            if player in self.players:
                continue

            self.players.append(player)
            result_list_to_string.append(player.name)

        return f"Successfully added: {', '.join(result_list_to_string)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player_name == player.name:
                return player

    def __find_supply_by_type(self, supplement_type):
        for idx in range(len(self.supplies) -1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == supplement_type:
                return idx, supply
        return -1, None

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)

        if player is None:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return

        index, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)
        self.supplies.pop(index)

        return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def duel_validator(*players):
        result = ''
        for player in players:
            if player.stamina == 0:
                result += f"Player {player.name} does not have enough stamina." + '\n'
        return result.strip()

    def duel(self, first_player_name: str, second_player_name: str):

        player_one = self.__find_player_by_name(first_player_name)
        player_two = self.__find_player_by_name(second_player_name)

        validate = self.duel_validator(player_one, player_two)
        if validate != '':
            return validate

        if player_two.stamina < player_one.stamina:
            player_one, player_two = player_two, player_one

        player_one_damage = player_one.stamina / 2
        player_two.stamina = max(player_two.stamina - player_one_damage, 0)

        if player_two.stamina == 0:
            return f"Winner: {player_one.name}"

        player_two_damage = player_two.stamina / 2
        player_one.stamina = max(player_one.stamina - player_two_damage, 0)

        if player_one.stamina == 0:
            return f"Winner: {player_two.name}"

        winner = player_one if player_one.stamina > player_two.stamina else player_two
        return f"Winner: {winner.name}"

    def next_day(self):

        for player in self.players:

            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):

        return '\n'.join([str(player) for player in self.players]) + '\n'\
               + '\n'.join([supply.details() for supply in self.supplies])




