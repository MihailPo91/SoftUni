import unittest

from project.movie import Movie


class TestMovie(unittest.TestCase):
    MOVIE_NAME = 'Test Movie'
    MOVIE_YEAR = 1999
    MOVIE_RATING = 9.0

    def setUp(self) -> None:
        self.movie = Movie(self.MOVIE_NAME, self.MOVIE_YEAR, self.MOVIE_RATING)

    def test_init__name_with_an_empty_string__expect_to_raise(self):
        with self.assertRaises(ValueError) as error:
            movie = Movie('', self.MOVIE_YEAR, self.MOVIE_RATING)

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_init__name_with_correct_input__expect_correct_name(self):
        self.assertEqual(self.MOVIE_NAME, self.movie.name)

    def test_init__year_with_invalid_value__expect_to_raise(self):
        with self.assertRaises(ValueError) as error:
            movie = Movie(self.MOVIE_NAME, 1800, self.MOVIE_RATING)

        self.assertEqual("Year is not valid!", str(error.exception))

    def test_init__year_with_correct_value__expect_to_create_year(self):
        self.assertEqual(self.MOVIE_YEAR, self.movie.year)

    def test_init__rating_expect_to_be_correct(self):
        self.assertEqual(self.MOVIE_RATING, self.movie.rating)

    def test_init__actors_list__expect_to_be_empty_list_on_initialisation(self):
        self.assertEqual([], self.movie.actors)

    def test_add_actor_when_actor_already_in_the_list__expect_to_message(self):
        actor_name = 'Al Pacino'
        self.movie.add_actor(actor_name)
        result = self.movie.add_actor(actor_name)

        self.assertEqual(f"{actor_name} is already added in the list of actors!", result)
        self.assertEqual(['Al Pacino'], self.movie.actors)

    def test_add_actor_expect_to_add_actor_name_to_list(self):
        actor_name = 'Al Pacino'
        self.movie.add_actor(actor_name)

        self.assertEqual(['Al Pacino'], self.movie.actors)

    def test_dunder_gt__with_2_movies_expect_correct_comparison(self):
        another_movie = Movie('Another', 2001, 7.0)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie

        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie.name}"', first_result)
        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie.name}"', second_result)

    def test_repr__expect_correct_result(self):
        actors = ['Gosho', 'Pesho']
        self.movie.actors = actors
        result = repr(self.movie)
        expected_result = f"Name: {self.MOVIE_NAME}\n" \
                          f"Year of Release: {self.MOVIE_YEAR}\n"\
                          f"Rating: {self.MOVIE_RATING:.2f}\n"\
                          f"Cast: {', '.join(actors)}"

        self.assertEqual(expected_result, result)