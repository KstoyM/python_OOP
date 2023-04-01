from typing import List

from movie_app.movie_specification.movie import Movie
from movie_app.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def find_user_by_username(self, username):
        current_user = next(filter(lambda x: x.username == username, self.users_collection), None)
        if not current_user:
            raise Exception("This user does not exist!")
        return current_user

    def is_user_owner_of_movie(self, username, movie: Movie):
        current_user = self.find_user_by_username(username)
        if current_user.username == movie.owner.username:
            return True
        else:
            return False

    def register_user(self, username: str, age: int):
        current_user = next(filter(lambda x: x.username == username, self.users_collection), None)
        if current_user:
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        current_user = self.find_user_by_username(username)

        if not self.is_user_owner_of_movie(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        current_user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        self.is_user_owner_of_movie(username, movie)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not self.is_user_owner_of_movie(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)
        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie):
        current_user = self.find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not self.is_user_owner_of_movie(username, movie):
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        current_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        current_user = self.find_user_by_username(username)
        if movie.owner != current_user:
            if movie not in current_user.movies_liked:
                movie.likes += 1
                current_user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."
            else:
                raise Exception(f"{username} already liked the movie {movie.title}!")
        else:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

    def dislike_movie(self, username, movie):
        current_user = self.find_user_by_username(username)
        if movie in current_user.movies_liked:
            movie.likes -= 1
            current_user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."
        else:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        if self.movies_collection:
            sorted_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
            result = '\n'.join([movie.details() for movie in sorted_collection])
            return result
        return "No movies found."

    def __str__(self):
        all_users = ', '.join(user.username for user in self.users_collection)
        all_movies = ', '.join(movie.title for movie in self.movies_collection)
        result_users = f'All users: ' + all_users + '\n' if all_users else 'All users: No users.\n'
        result_movies = f'All movies: ' + all_movies if all_movies else 'All movies: No movies.'
        return result_users + result_movies
