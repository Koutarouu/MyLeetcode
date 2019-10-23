# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None: return head
        t=head
        while t.next:
            if t.val==t.next.val:
                t.next=t.next.next
            else:
                t=t.next
        return head