class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxOnes = 0
        count = 0
        
        for digit in nums:
            if digit == 1:
                count += 1
            else:
                count = 0

            maxOnes = max(maxOnes, count)

        return maxOnes