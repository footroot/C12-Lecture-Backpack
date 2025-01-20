# Simulations of methods overloading in Python with args and kwargs

def add(*args):
    """
    Description: 
        This function adds all the arguments passed to it.
    Args:
        *args: Regardless of the number of arguments passed, this function will add them all.
        This simulation is similar to method overloading in other languages. 

    Returns:
        int : The sum of all the arguments passed to the function.
        float : The sum of all the arguments passed to the function.
    """
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2))

def print_name(**kwargs):
    """
    Description:
        This function prints the names passed to it.
    Args:
        **kwargs: Regardless of the number of keyword arguments passed, this function will print them all.
        This simulation is similar to method overloading in other languages.
    """
    for _, value in kwargs.items():
        print(f"The names are {value}")

print_name(name1="Alice", name2="Bob", name3="Charlie")