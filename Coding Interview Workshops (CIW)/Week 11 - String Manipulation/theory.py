# Common String Manipulation Techniques:
# - Substrings: splicing, substring -> string[start=0:stop=-1:step=1], string.slice(start, stop, step)
# - Character access: indexing, charAt() -> string[indexOfChar], charAt(index)
# - Concatenation: combining strings -> +, +=, string.join(joinString)
# - Searching: find location of substring -> string.find("substring"), 
# substring in string, string.includes(substring), string.indexOf(substring)
# - Replacement and Case Conversion: string.replace(replace, with), replaceAll, 
# lower(), upper(), toLowerCase(), toUpperCase()
# - Reversing: .reverse(), [start=-1:stop=0:-1]

# Optimization Approaches:
# - Sliding Window Technique - Dynamic Programming (technically)
# Maintain a window [start ... end]
# Slide across the string

'''[1, 2, 3, 4, 5] -> k = 3
6
6 + 4 - 1 = 9
9 + 5 - 2 = 12

[happy birthdy] -> [birthday]
'''

def sliding_window(s, k):
    max_sum = 0
    current_sum = sum(s[:k])
    for i in range(k, len(s)):
        current_sum += s[i] - s[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# - Two Pointer Technique - Dynamic Programming
# Palidromes 

# - Hash Maps - Character Frequencies
# Keeping track of the number of characters in each string
from collections import Counter

s = "anagram"
count = Counter(s)
print(count['a'])  # 3

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Time & Space Complexity of String Methods:
# - Accessing: O(1)
# - Slicing: O(k) (k is the length of your substring)
# - Comparison: O(n) "hello"=="world"
# - Concatenation: O(n) -> O(n^2)
 

