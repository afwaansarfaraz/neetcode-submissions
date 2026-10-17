# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            next_node = current.next # Save the next node
            current.next = prev # Reverse the link
            prev = current # Move prev forward
            current = next_node # Move current forward
        return prev