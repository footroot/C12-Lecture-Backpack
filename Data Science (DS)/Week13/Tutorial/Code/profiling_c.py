import cProfile

def example_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Profile the execution of the function
cProfile.run('example_function()')

