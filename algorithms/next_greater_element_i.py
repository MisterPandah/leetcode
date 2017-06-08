class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        solution = []
        
        for x in findNums:
            notFound = True
            for i in nums[nums.index(x):]:
                if i > x:
                    solution.append(i)
                    notFound = False
                    break
            
            if notFound:
                solution.append(-1)
        
        return solution