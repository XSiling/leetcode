# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cnt = 0
        node = head
        while node != None:
            cnt += 1
            node = node.next

        node = head
        for i in range(cnt - k):
            node = node.next
        
        return node
