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
