from abc import ABC, abstractmethod

# Abstract class for a product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete class for Dog
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Concrete class for Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Concrete class for Cow
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Factory class to create Animal objects
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "cow":
            return Cow()
        else:
            raise ValueError("Unknown animal type")

# Client code
if __name__ == "__main__":
    factory = AnimalFactory()

    # Create a dog
    dog = factory.create_animal("dog")
    print(f"Dog says: {dog.speak()}")

    # Create a cat
    cat = factory.create_animal("cat")
    print(f"Cat says: {cat.speak()}")

    # Create a cow
    cow = factory.create_animal("cow")
    print(f"Cow says: {cow.speak()}")
