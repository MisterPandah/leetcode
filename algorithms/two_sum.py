class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        table = {}
        
        for i in range(len(nums)):
            
            if target-nums[i] in table:
                return [table[target-nums[i]][0],i]
            
            # Add/Append to table if does not exist
            if nums[i] in table:
                # Duplicates can appear in the array
                table[nums[i]].append(i)
            else:
                # Initialize the entry as a list
                table[nums[i]] = [i]