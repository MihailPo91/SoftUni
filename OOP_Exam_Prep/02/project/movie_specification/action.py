from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    DEFAULT_AGE_RESTRICTION = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.DEFAULT_AGE_RESTRICTION:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"


