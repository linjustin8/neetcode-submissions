# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        sentinel = ListNode(-1, None)
        minHeap = [] # [[node.val, node, listIndex]]

        for listIndex in range(len(lists)):
            if lists[listIndex]:
                minHeap.append([lists[listIndex].val, listIndex, lists[listIndex]])

        if not minHeap:
            return None

        heapq.heapify(minHeap)
        sentinel.next = minHeap[0][2]
        head = sentinel

        while minHeap:
            value, listIndex, node = heapq.heappop(minHeap)
            head.next = node
            head = head.next

            node = node.next
            if node:
                heapq.heappush(minHeap, [node.val, listIndex, node])
        
        return sentinel.next

