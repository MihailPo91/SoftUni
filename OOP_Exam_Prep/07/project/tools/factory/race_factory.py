from project.race import Race


class RaceCreator:

    @staticmethod
    def create_race(race_name: str):
        return Race(race_name)
