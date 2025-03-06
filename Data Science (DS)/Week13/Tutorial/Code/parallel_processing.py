from joblib import Parallel, delayed
import time

def slow_function(x):
    time.sleep(1)
    return x * x

# Run the function in parallel using 4 CPU cores
results = Parallel(verbose=100, n_jobs=4)(delayed(slow_function)(i) for i in range(10))
print(results)

