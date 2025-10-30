students = [
    ["Peter", "Parker", 23],
    ["Mia", "Mitchelle", 28],
    ["Karl", "James", 24],
    ["Jack", "Jackson", 29]
]

class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Value not changed. Incorrect data type provided!")

    def greet(self):
        print(f"Hello, my name is {self.name}. Welcome to town!")

    def display_info(self):
        info = "Personal Information:\n"
        info += f"Name: {self.name}\nSurname: {self.surname}\n"
        info += f"Age: {self.age}"
        print(info)

people = [
    Person("Peter", "Parker", 23),
    Person("Mia", "Mitchelle", 28),
    Person("Karl", "James", 24),
    Person("Jack", "Jackson", 29)
]

for person in people:
    print(f"{person.name} {person.surname}")



# person1 = Person("Jason", "Jackson", 34)
# # print(person1.name)
# # print(person1.surname)
# # print(person1.age)

# person1.display_info()

person2 = Person("Peter", "Parker", 35)
person2.set_name("Tina")
person2.display_info()