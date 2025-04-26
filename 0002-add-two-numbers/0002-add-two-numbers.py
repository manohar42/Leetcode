# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lis1 = []
        lis2 = []
        while l1 is not None:
            lis1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            lis2.append(l2.val)
            l2 = l2.next
        
        num1 = 0
        num2 = 0
        i = -1
        while i >= -1*len(lis1):
            num1 = num1*10+lis1[i]
            i-=1
        i = -1
        while i >= -1*len(lis2):
            num2 = num2*10+lis2[i]
            i-=1
        result = num1+num2
        count = 0
        head = l1
        if result == 0:
            head = ListNode(0)
        while result > 0:
            k = result%10
            l = ListNode(k)
            result = result//10
            count+=1
            if count == 1:
                head = l
                l1 = head
            else:
                l1.next = l
                l1 =l1.next
                
        return head