from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_username = {}

    def register_user(self, username: str, age: int):
        user = self.__get_user_by_username(username)
        if user:
            raise Exception("User already exists!")

        user = User(username, age)

        self.users_collection.append(user)
        self.users_by_username[user.username] = user
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if user is None:
            raise Exception("This user does not exist!")

        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for m in self.movies_collection:
            if m == movie:
                raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user_by_username(username)

        target_movie = [m for m in self.movies_collection if m == movie]
        if not target_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        movie.title = kwargs.get('title', movie.title)
        movie.year = kwargs.get('year', movie.year)
        movie.age_restriction = kwargs.get('age_restriction', movie.age_restriction)

        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        target_movie = [m for m in self.movies_collection if m == movie]
        if not target_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        if user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for m in user.movies_liked:
            if m == movie:
                raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)

        target_movie = [m for m in user.movies_liked if m == movie]
        if not target_movie:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        result = '\n'.join([movie.details() for movie in sorted_movies])
        return result

    def __str__(self):
        result_string = ''
        if not self.users_collection:
            result_string += "All users: No users." + '\n'
        else:
            result_string += 'All users: ' + ', '.join([user.username for user in self.users_collection]) + '\n'

        if not self.movies_collection:
            result_string += "All movies: No movies." + '\n'
        else:
            result_string += 'All movies: ' + ', '.join([movie.title for movie in self.movies_collection]) + '\n'
        return result_string.strip()

    def __get_user_by_username(self, username) -> User:
        return self.users_by_username.get(username, None)


