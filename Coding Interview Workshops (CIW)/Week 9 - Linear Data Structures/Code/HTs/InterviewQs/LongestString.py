class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        maxLen = 0
        i = 0
        newStart = 1

        while i < len(s):
            char = s[i]
            if (not (char in substring)):
                substring.append(char)
                i += 1
            else:
                if len(substring) > maxLen:
                    maxLen = len(substring)
                substring = []
                i = newStart
                newStart += 1


        return maxLen