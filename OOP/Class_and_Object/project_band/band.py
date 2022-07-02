from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for item in self.albums:
            if item == album:
                return f"Band {self.name} already has {item.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if album.published:
                return "Album has been published. It cannot be removed."
            if album.name == album_name:
                self.albums.remove(album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result_string = f'Band {self.name}\n'
        for album in self.albums:
            result_string += f'{album.details()}\n'
        return result_string


album = Album("The Sound of Perseverance")
song = Song("Scavenger of Human Sorrow", 6.56, True)
album.add_song(song)