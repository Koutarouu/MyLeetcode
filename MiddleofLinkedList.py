class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast=head
        while fast and fast.next:
            head=head.next
            fast=fast.next.next
        return head
    def middleNode(self, head: ListNode) -> ListNode:
        l=0
        temp=head
        while head:
            l+=1
            head = head.next
        l //= 2
        while l:
            temp = temp.next
            l-=1
        return temp