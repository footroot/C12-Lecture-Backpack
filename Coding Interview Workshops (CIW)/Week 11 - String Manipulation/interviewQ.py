# 1. Assumptions
# ignore whitespace
# - sign
# ignore leading 0
# rounding


# 2. Plan
# strip(string)
# check [0] == - -> -1, + -> 1, 1 (sign variable), pop sign after
# strip(0)
# for the rest of the string check [0] is ["0-9"] -> add to number 
# convert to int

# 3. Code

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        if s == "":
            sign = 0
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1

        
        digit = ""
        s.strip("0")
        for i in s:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                digit += i
            else:
                break
        
        if digit == "":
            return 0
        else:
            if int(digit) >= 2**31:
                if sign == 1:
                    return 2**31 - 1
                else:
                    return 2**31 * sign 
            else:
                return int(digit) * sign
         

        