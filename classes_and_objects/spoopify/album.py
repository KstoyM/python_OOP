from typing import Tuple

from spoopify.song import Song


class Album:

    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = list(*songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            try:
                song = next(filter(lambda s: song_name == s.name, self.songs))
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
            except StopIteration:
                return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        result = "\n".join([f'== {s.get_info()}' for s in self.songs])
        return f"Album {self.name}\n" \
               f"{result}"


