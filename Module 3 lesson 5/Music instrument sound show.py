from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat

    def display_info(self):
        print(f"instrument name: {self.name}")
        print(f"category: {self.cat}")

    @abstractmethod
    def play_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name, cat, strings):
        super().__init__(name, cat)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} has {self.strings} strings and sounds like: strum strum!")

class Drum(Instrument):
    def __init__(self, name, cat, dtype):
        super().__init__(name, cat)
        self.dtype = dtype

    def play_sound(self):
        print(f"{self.name} is a {self.dtype} and sounds like: boom boom!")

class Flute(Instrument):
    def __init__(self, name, cat, mat):
        super().__init__(name, cat)
        self.mat = mat

    def play_sound(self):
        print(f"{self.name} is made of {self.mat} and sounds like: toot toot!")

g = Guitar("acoustic guitar", "string instrument", 6)
d = Drum("bass drum", "percussion instrument", "large drum")
f = Flute("bamboo flute", "wind instrument", "bamboo")

g.display_info()
g.play_sound()

print()

d.display_info()
d.play_sound()

print()

f.display_info()
f.play_sound()