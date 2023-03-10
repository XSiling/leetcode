# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result = []
        node = head
        while node != None:
            result.append(node.val)
            node = node.next
        
        return result[::-1]
