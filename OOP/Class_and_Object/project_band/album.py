from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.published = False
        self.songs = []
        if args:
            for item in args:
                self.songs.append(item)

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        for item in self.songs:
            if item == song:
                return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for item in self.songs:
            if item.name == song_name:
                self.songs.remove(item)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result_string = f'Album {self.name}\n'
        for song in self.songs:
            result_string += f'=={song.get_info()}\n'
        return result_string
