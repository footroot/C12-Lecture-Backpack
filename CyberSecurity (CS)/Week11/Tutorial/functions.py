def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return "Invalid input."
    return (celsius * 9/5) + 32

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
