# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        prev = None
        new_head = head
        while current:
            if current.val == val:
                if prev is None:
                    new_head = current.next
                else:
                    prev.next = current.next
            else:
                prev = current
            current = current.next
        return new_head