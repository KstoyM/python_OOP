from spoopify.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        try:
            album = next(filter(lambda a: album_name == a.name, self.albums))
            if album.published:
                return f"Album has been published. It cannot be removed."
            else:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        except StopIteration:
            f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" \
               + "\n".join([a.details() for a in self.albums])
