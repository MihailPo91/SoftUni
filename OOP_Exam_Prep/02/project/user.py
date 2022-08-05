import os


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        movies_liked_str = 'No movies liked.'
        if self.movies_liked:
            movies_liked_str = os.linesep.join(m.details() for m in self.movies_liked)

        movies_owned_str = 'No movies owned.'
        if self.movies_owned:
            movies_owned_str = os.linesep.join(m.details() for m in self.movies_owned)

        return f'''Username: {self.username}, Age: {self.age}
        Liked movies:
        {movies_liked_str}
        Owned movies:
        {movies_owned_str}'''
