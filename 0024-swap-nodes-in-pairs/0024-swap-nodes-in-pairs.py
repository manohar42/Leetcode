# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        cur = dummy
        while head and head.next:
            node1 = head
            node2 = head.next
            head = head.next
            node1.next = head.next
            node2.next = node1
            cur.next = node2
            head = head.next.next
            cur = cur.next.next

        return dummy.next