# Author: Prinika Sankaran Nair
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head
        
        if current == None:
            return head
        
        while current.next != None:
            aftercurrent = current.next
            if current.val == aftercurrent.val:
                current.next = aftercurrent.next
            else:
                current = current.next

        return head
