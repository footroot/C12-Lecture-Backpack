# Challenge 1
# Refactor the code to be less redundant
def greet(name):
    if name:
        return "Hello, " + name + "!"
    else:
        return "Hello, World!"


def greet(name):
    return f"Hello, {name}!" if name else "Hello, World!"






# Challenge 2
# Refactor the code by simplifying the conditional.
def get_discounted_price(price, is_member):
    if is_member == True:
        discount = 0.1
    else:
        discount = 0.05
    return price - (price * discount)

MAX_DISCOUNT = 0.1
MIN_DISCOUNT = 0.05

def get_discounted_price(price, is_member):
    discount = MAX_DISCOUNT if is_member else MIN_DISCOUNT
    return price - (price * discount)


# print(get_discounted_price(20, False))















# Challenge 3
# Refactor the code to make in more readable and not use nested statements.
def check_access(user):
    if user:
        if user["role"] == "admin":
            if user["active"]:
                return "Access granted"
    return "Access denied"


def check_access(user):
    if user and user.get("role") == "admin" and user.get("active"):
        return "Access Granted!"
    return "Access Denied!"















# Challenge 4
# Refactor the code to implement OOP
def get_employee_salary(employee_type, hours_worked):
    if employee_type == "full_time":
        return hours_worked * 50
    elif employee_type == "part_time":
        return hours_worked * 30
    else:
        return hours_worked * 20


class Employee:
    def __init__(self, hours_worked) -> None:
        self.hours_worked = hours_worked
        self.hourly_rate = None

    def get_salary(self):
        return self.hours_worked * self.hourly_rate


class FullTimeEmployee(Employee):
    def __init__(self, hours_worked) -> None:
        super().__init__(hours_worked)
        self.hourly_rate = 50

class PartTimeEmployee(Employee):
    def __init__(self, hours_worked) -> None:
        super().__init__(hours_worked)
        self.hourly_rate = 30

class Contractor(Employee):
    def __init__(self, hours_worked) -> None:
        super().__init__(hours_worked)
        self.hourly_rate = 20

fulltime = FullTimeEmployee(20)
parttime = PartTimeEmployee(20)
contractor = Contractor(20)

print(fulltime.get_salary())
print(parttime.get_salary())
print(contractor.get_salary())













# Challenge 5
# Refactor this function to use a dictionary mapping instead of 
# multiple if statements. 
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


