class Robot:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hello, my name is {self.name}!")
robot1 = Robot("tom")
robot2 = Robot("jerry")
robot1.introduce()
robot2.introduce()
