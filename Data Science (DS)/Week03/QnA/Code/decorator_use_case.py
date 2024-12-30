def validator(func):
    """
    This is a decorator function called 'validator'. Decorators are a way to modify or enhance functions in Python without directly changing their code.

    Here's how this decorator works:

    1. It takes a function ('func') as input. This is the function we want to decorate (e.g., 'multiply' or 'add').

    2. It defines an inner function called 'wrapper'. This 'wrapper' function is crucial. It's what actually gets executed when you call the decorated function.

    3. Inside 'wrapper', we perform some actions (in this case, checking if 'a' and 'b' are negative).

    4. If the condition (a < 0 and b < 0) is true, 'wrapper' returns a specific message.

    5. Otherwise, 'wrapper' calls the original function ('func') with the given arguments ('a' and 'b'), stores the result in 'output', and returns that result.

    6. Finally, the 'validator' function returns the 'wrapper' function. This is the key to how decorators work: you're essentially replacing the original function with this modified 'wrapper' function.

    The relationship between the wrapper and decorators:
    The wrapper function is the core of the decorator's functionality. When you use the @validator syntax (e.g., @validator above the multiply function), you're telling Python to do the following:

        multiply = validator(multiply)

    This means the multiply function is passed as an argument to the validator function. The validator function then returns the wrapper function. Therefore, the multiply function is now pointing to the wrapper function. When you subsequently call multiply, you're actually executing the wrapper function. The wrapper function then decides whether to call the original multiply function or return a specific message. This is how decorators modify the behavior of functions.
    """
    def wrapper(a, b):
        """
        This is the inner 'wrapper' function. It's what gets executed when you call a decorated function.

        It performs the validation check: if both 'a' and 'b' are negative, it returns a message. Otherwise, it calls the original function and returns its result.
        """
        if a < 0 and b < 0:
            return "a and b are all Negative"
        else:
            output = func(a, b) # Call the original function if the validation passes
            return output
    return wrapper # Return the wrapper function

"""
Uncomment the @validator decorator to see the output. 
If not uncommented, the output will be the same as the function output. Any number that is negative will return the message "a and b are all Negative"
@validator calls the wrapper function which checks if a and b are negative.
If @validator is left commented, the output will be the same as the function output. Therfore all numbers, including negative numbers will be returned. as normal.
"""

@validator # Applying the validator decorator to the multiply function
def multiply(a=0, b=0):
    """
    This function multiplies two numbers together.
    a: The first number. Default is 0
    b: The second number. Default is 0
    return: The product of a and b
    """
    result = a * b
    return result

@validator # Applying the validator decorator to the add function
def add(a=0, b=0):
    """
    This function adds two numbers together.
    a: The first number. Default is 0
    b: The second number. Default is 0
    return: The sum of a and b
    """
    result = a + b
    return result

"""
The validator function is a decorator that checks if the numbers are negative. If they are, it will return a message. You can see 2 prints functions below. 
The first print function is the function output. The second print function is the validator output, which is the first principle of the decorator.

If the second print is uncommented, the output will be the message "a and b are all Negative" because the numbers are negative. If will act as a validator to the function that is being passed as an argument.
"""

print("This is the add: ",add(-2, -5)) # Calls the decorated 'add' function (which executes the 'wrapper')
# print("This is the validator: ",validator(add)(-2, -5)) # Demonstrates calling the validator directly (less common)

print("This is the multiplication: ",multiply(-2, -5)) # Calls the decorated 'multiply' function (which executes the 'wrapper')
# print("This is the validator: ",validator(multiply)(-2, -5)) # Demonstrates calling the validator directly (less common)