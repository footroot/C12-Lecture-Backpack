def example3(n):
    count = 0                   # O(1)

    i = n                       # O(1)

    while i > 1:                # O(log n)
        for j in range(n):      # O(n)
            count += j
        i //= 2                 # O(1)

    for k in range(n):          # O(n)
        count += k

    count += 7                  # O(1)
    
    return count

#   1 + 1 + nlogn + n + 1
#   nlogn + n + 3
# O(nlogn)

def example4(n):
    if n <= 1:
        return 1

    result = example4(n - 1) + example4(n - 2)

    for i in range(n):
        for j in range(n):
            result += i * j
    
    return result






















def example5(n):
    count = 0                   # O(1)

    for i in range(n):          # O(n)
        for j in range(n):      # O(n)
            count += i * j  

    i = n                       # O(1)
    while i > 1:                # O(logn)
        for j in range(n):      # O(n)
            count += j          # O(1)
        i //= 2                 # O(1)

    count += 10                 # O(1)
    
    return count

#   1 + n^2 + nlogn + 1
#   n^2 + nlogn + 2
#   O(n^2)