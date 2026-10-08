class ArtGallery:

    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []

        print(f"\nwelcome to {self.gallery_name}!")
        print(f"location: {self.location}.")
        print("art gallery collection is ready.")

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the gallery collection.")

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has been removed from the gallery collection.")
        else:
            print(f"'{artwork}' was not found in the gallery collection.")

    def display_artworks(self):
        print(f"\n--- {self.gallery_name} art collection ---")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("no artworks have been added yet.")

    def __del__(self):
        print(f"\nclosing {self.gallery_name}. thank you for managing the art collection!")


gallery = ArtGallery("creative canvas gallery", "bengaluru")

while True:
    print("\n========= art gallery menu =========")
    print("1. add artwork")
    print("2. remove artwork")
    print("3. display art collection")
    print("4. exit")
    print("===================================")

    choice = input("enter your choice (1-4): ")

    if choice == "1":
        artwork_name = input("enter the artwork name to add: ")
        gallery.add_artwork(artwork_name)

    elif choice == "2":
        artwork_name = input("enter the artwork name to remove: ")
        gallery.remove_artwork(artwork_name)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        print("exiting the art gallery collection manager...")
        del gallery
        break

    else:
        print("invalid choice! please enter a valid option from 1 to 4.")