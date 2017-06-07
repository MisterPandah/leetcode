class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        # A count of the hamming distance
        distCount = 0
        
        # Applying bitwise xor wil result 
        diffBits = x ^ y
        
        while diffBits:
            # Update the count if the least-significant bit is 1
            distCount += diffBits & 1
            
            diffBits = diffBits >> 1
            
        return distCount