# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle
        slow = fast = head 
        while fast.next and fast.next.next:
            slow =slow.next
            fast = fast.next.next
        # 2. Split the list
        second = slow.next
        slow.next = None
        # 3. Reverse the second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        # 4. Merge both halves alternately
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2    

        