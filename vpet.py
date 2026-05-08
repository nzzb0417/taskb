# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is passed, at minimum, for the __init__ method

class VirtualPet:
    def __init__(self, name, energy=10, hunger=0):
        self.name = name
        self.energy = energy
        self.hunger = hunger

# This class has the following methods:
# (1) play() - If energy < 2, report in the format "{name} is too tired to play!"
# Otherwise simulate playing by reducing the energy by 2 and increase the hunger by 2
# (2) feed() - Simulate feeding the pet and reducing hunger by 1
# If hunger is less than 0, report in the format "{name} is overfed!" and reset hunger to 0
# (3) sleep() - Let the pet sleep and increase the energy by 10
# (4) __str__() - returns the details of the pet in the format "{name} has {energy} energy points and hunger level {hunger}"
# (5) __eq__() - returns true if all attributes are identical, false otherwise.

    def play(self):
        if self.energy < 2:
            return f"{self.name} is too tired to play!"
        else:
            self.energy = self.energy - 2
            self.hunger = self.hunger + 2

    def feed(self):
        self.hunger = self.hunger - 1
        if self.hunger < 0:
            self.hunger = 0
            return f"{self.name} is overfed!"

    def sleep(self):
        self.energy = self.energy + 10

    def __str__(self):
        return f"{self.name} has {self.energy} energy points and hunger level {self.hunger}"

    def __eq__(self, Pet1):
        if self.name == Pet1.name and self.energy == Pet1.energy and self.hunger == Pet1.hunger:
            verdict = True
        else:
            verdict = False
        return verdict

# You should test each method in your code before submission.
# Check that attributes are modified as expected
# For example:

Pet = VirtualPet("Emma", 5, 2)

Pet.play()
print(Pet)
print(Pet.feed()) # Added print to see the "overfed" message if it triggers
print(Pet)
