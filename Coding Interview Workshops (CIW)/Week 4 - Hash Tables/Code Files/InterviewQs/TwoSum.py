class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1::]):
                if ((num1 + num2) == target):
                    return [i, j+i+1]
        """

        hashT = {}

        for i, num1 in enumerate(nums):
            comp = target - num1
            if (comp in hashT):
                return [hashT[comp], i]
            else:
                hashT[num1] = i

            