# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        cur = dummy
        start = head
        while start and start.next:
            node1 = start
            node2 = start.next
            start = start.next
            node1.next = start.next

            node2.next = node1
            cur.next = node2
            print(cur,start)
            start = start.next.next
            cur = cur.next.next

        return dummy.next