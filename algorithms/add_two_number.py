# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Edge cases
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        
        full_add = l1.val+l2.val
        half_add = full_add%10
        carry_add = full_add/10
        
        # Initialize list to return
        dummy = ListNode(half_add)
        l3 = dummy
        
        while l1.next != None or l2.next != None:
            full_add = carry_add
            
            if l1.next != None:
                full_add = full_add + l1.next.val
                l1 = l1.next
            
            if l2.next != None:
                full_add = full_add + l2.next.val
                l2 = l2.next

            half_add = full_add%10
            carry_add = full_add/10
            
            l3.next = ListNode(half_add)
            l3 = l3.next
        
        if carry_add != 0:
            l3.next = ListNode(carry_add)
        
        return dummy