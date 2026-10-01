class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print (f"Playlist '{self.name}' ({self.genre}) is ready!")

    def add_songs(self,song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")
    def remove_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                print (f"''{song}' removed.")
            else:
                print("'{song}' removed.")
                
                print("'{song}' not found in playlist.")
    def display(self):
        print(f"\n---{self.name} ({self.genre})---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                   print(f" {i}. {song}")           
        else:
            print(" No songs yer, add some!")
    def __del__(self):
          print(f"Playlist '{self.name}' has been deleted. goodbye!")
my_playlist = Playlist("road trip mix","pop")

while True:
    print("\n1. Add song 2. remove song 3. view playlist 4. delete and quit")
    choice = input("enter your choice:")
    if choice == "1":
          song = input ("enter song name: ")
    elif choice == "2":
        song = input("enter song to remove:: ")
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("invalid choice. Enter 1,2,3, or 4")