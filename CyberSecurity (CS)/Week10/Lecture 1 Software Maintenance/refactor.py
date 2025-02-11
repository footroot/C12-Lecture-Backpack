# Challenge 1
numbers = [1, 2, 3, 4, 5]
squared = []
even_numbers = []

for num in numbers:
    squared.append(num ** 2)
    if num % 2 == 0:
        even_numbers.append(num)

print("Squared:", squared)
print("Even numbers:", even_numbers)














# Challenge 2
def check_permission(user):
    if user.role == "admin":
        return "Full access granted"
    elif user.role == "editor":
        return "Edit access only"
    elif user.role == "viewer":
        return "Read-only access"
    else:
        return "Invalid role"
    
# Challenge 3
# Redundant animal classes
class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"