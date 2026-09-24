class student:
    grade = 10
    name = "prishab"

    def introduction(self):
        print("hi I am a student")

    def details(self):
        print("my name is", self.name)
        print("I am in grade", self.grade)
ob = student()
ob.introduction()
ob.details()