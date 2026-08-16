# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = []
        sentinel = ListNode(-1, head)
        prev = sentinel
        while head:
            curr.append(head)
            nxt = head.next
            if len(curr) == k:
                newHead = self.reverse(curr[0], nxt)
                prev.next.next = nxt
                prev.next = newHead
                prev = curr[0]
                curr = []
            head = nxt
        
        return sentinel.next
    
    def reverse(self, head, end):
        if not head:
            return head
        
        prev = None
        while head and head != end:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return prev