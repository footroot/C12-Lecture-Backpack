# This code demonstrates creating a Human class in Python.

# A class is like a blueprint for creating objects that represent real-world things.
# In this case, the Human class represents a person.

# Class attribute (shared by all Human objects)
class Human:
    species = "Homo sapiens"  # This is a shared characteristic of all humans in this program.

    # Constructor (initializer) - This special method runs whenever you create a new Human object.
    def __init__(self, name, age, occupation):
        # Instance attributes (data specific to each Human object)
        self.name = name  # Stores the name of the specific person (object).
        self.age = age  # Stores the age of the specific person.
        self.occupation = occupation  # Stores the occupation of the specific person.
        self.energy = 100  # Tracks the current energy level of the person (starts at 100).

    # Instance methods (functions specific to Human objects)
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a {self.age}-year-old {self.occupation}.")
        # This method allows the person (object) to introduce themselves using their attributes.

    def work(self, hours):
        if self.energy >= hours * 10:  # Working costs energy (10 per hour)
            print(f"{self.name} worked for {hours} hours.")
            self.energy -= hours * 10  # Update energy level after working.
        else:
            print(f"{self.name} is too tired to work that much.")
        # This method simulates working, checking energy and updating it if possible.

    def rest(self, hours):
        self.energy += hours * 15  # Resting restores energy (15 per hour, capped at 100)
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} rested for {hours} hours. Energy is now {self.energy}.")
        # This method simulates resting, increasing energy with a cap.

    def get_older(self, years):
        self.age += years
        print(f"{self.name} is now {self.age} years old.")
        # This method simulates aging the person (object) by updating their age.

# Create Human objects (instances of the Human class)
alice = Human("Alice", 30, "Software Engineer")
bob = Human("Bob", 25, "Teacher")
charlie = Human("Charlie", 40, "Doctor")

# Call methods on the objects (tell the objects to do something)
alice.introduce()  # Output: Hello, my name is Alice. I am a 30-year-old Software Engineer.
bob.work(5)  # Output: Bob worked for 5 hours.
bob.rest(2)  # Output: Bob rested for 2 hours. Energy is now 80.
charlie.work(12)  # Output: Charlie is too tired to work that much.
charlie.rest(5)  # Output: Charlie rested for 5 hours. Energy is now 100.
alice.get_older(1)  # Output: Alice is now 31 years old.

# Access attributes (data) of the objects
print(f"{alice.name}'s occupation is {alice.occupation}.")  # Output: Alice's occupation is Software Engineer.
print(Human.species)  # Output: Homo sapiens (access class attribute)
print(bob.species)  # Output: Homo sapiens (access class attribute)