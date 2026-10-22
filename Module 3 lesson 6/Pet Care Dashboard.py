class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def show_info(self):
        print(f"pet name: {self.name}")
        print(f"health level: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("health must be between 0 and 100.")


class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")


class Cat(Pet):
    def care_action(self):
        print(f"{self.name} needs grooming and quiet rest.")


class Rabbit(Pet):
    def care_action(self):
        print(f"{self.name} needs fresh carrots and a clean cage.")


dog = Dog("buddy", 85)
cat = Cat("misty", 75)
rabbit = Rabbit("snowy", 65)

pets = [dog, cat, rabbit]

print("===== my pet care dashboard =====\n")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()

print("===== updating pet health =====\n")

dog.set_health(90)
cat.set_health(80)
rabbit.set_health(70)

print("\n===== final pet care summary =====\n")

for pet in pets:
    pet.show_info()
    print()