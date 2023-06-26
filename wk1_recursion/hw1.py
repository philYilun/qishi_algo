from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        cur = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 or list2
        return pre_head.next



class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(n):
            if (n == 2) or (n == 1) :
                return True 
            elif n <= 0 :
                return False
            elif n % 2 == 0:
                return helper(n/2)
            else:
                return False
        return helper(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_tmp = ListNode()
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        
        if head.val == val:
            head = head.next
        
        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_tmp = ListNode()
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        
        if head.val == val:
            head = head.next
        
        return head
