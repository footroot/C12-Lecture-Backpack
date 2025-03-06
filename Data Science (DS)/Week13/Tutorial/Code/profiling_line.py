from line_profiler import LineProfiler


def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


# Create a profiler and add the function
lp = LineProfiler()
lp.add_function(slow_function)

# Run the profiler
lp.enable()
slow_function()
lp.disable()

# Print the profiling results
lp.print_stats()
