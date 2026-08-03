# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i, j = 0 - n, 1
        temp = head
        while temp:
            temp = temp.next
            j += 1
            i += 1 

        i, j = 0, i
        sentinel = ListNode(-1, head)
        prev = sentinel
        while i < j:
            prev = prev.next
            head = head.next
            i += 1
        
        prev.next = head.next
        return sentinel.next
    