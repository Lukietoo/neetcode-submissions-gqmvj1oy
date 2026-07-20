# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        counter = head
        while counter:
            counter = counter.next
            k = k + 1
        
        removeIndex = k - n
        if removeIndex == 0:
            return head.next
        
        counter = head
        for i in range(k - 1):
            if (i + 1) == removeIndex:
                counter.next = counter.next.next
                break
            counter = counter.next
        return head