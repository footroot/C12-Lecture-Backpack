def example1(n):
    total = 0                  # O(1)

    for i in range(n):         # O(n)
        for j in range(n):     # O(n)
            total += i * j  

    for k in range(n):         # O(n)
        total += k

    return total

#  O(n^2)















def example2(n):
    count = 0                          # O(1)

    for i in range(n):                 # O(n)
        for j in range(n):             # O(n)
            for k in range(n):         # O(n)
                count += i + j + k  

    for x in range(n):                 # O(n)
        count += x  

    count += 5                         # O(1)

    return count

#  O(n^3)
