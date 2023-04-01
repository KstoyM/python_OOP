class User:
    def __init__(self, username, age):
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
        liked_movies = "\n".join(movie.details() for movie in self.movies_liked)
        movies_owned = "\n".join(movie.details() for movie in self.movies_owned)
        return f"Username: {self.username}, Age: {self.age}\n" \
               f"Liked movies:\n{liked_movies if liked_movies else 'No movies liked.'}\n" \
               f"Owned movies:\n{movies_owned if movies_owned else 'No movies owned.'}"
