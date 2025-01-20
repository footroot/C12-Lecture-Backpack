def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())


def add_prefix_decorator(prefix):
    def decorator(func):
        def wrapper():
            return prefix + func()
        return wrapper
    return decorator

@add_prefix_decorator("Mr. ")
def name():
    return "Jackson"

print(name())