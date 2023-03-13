# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        TheNodeList = []
        node = head
        while node != None:
            TheNodeList.append(node.val)
            node = node.next
        
        return TheNodeList == TheNodeList[::-1]
