# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # find the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # split into two halves
        list2 = slow.next
        slow.next = None
        list1 = head

        # sort both halves
        list1 = self.sortList(list1)
        list2 = self.sortList(list2)

        # merge two sorted halves
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # attach the nodes if they are left
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next