# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

def insertNodeAtTail(head, data):
    temp = ListNode(data)
    if head==None:
        head = temp
        return head
    temp2 = head
    while temp2.next:
        temp2 = temp2.next
    temp2.next = temp
    return head

def Print(node):
  while node:
    print(node.val,end=' ')
    node = node.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp=res=ListNode(None)
        carry=0
        while l1 or l2:
            res.next=ListNode(None)
            res = res.next
            if l1 and l2:
                toadd = l1.val+l2.val+carry
                carry = toadd//10
                res.val=toadd%10
                l1=l1.next
                l2=l2.next
            elif l1:
                res.val = (l1.val+carry)%10
                carry = (l1.val+carry)//10
                l1 = l1.next
            else:
                res.val = (l2.val+carry)%10
                carry = (l2.val+carry)//10
                l2 = l2.next
        if carry:
            res.next=ListNode(carry)
        return temp.next

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        exp=0
        number=0
        while l1:
            number+=l1.val*(10**exp)
            exp+=1
            l1=l1.next
        exp=0
        while l2:
            number+=l2.val*(10**exp)
            exp+=1
            l2=l2.next
        rn=number
        temp=res=ListNode(0)
        while rn>0:
            res.val = rn%10
            rn//=10
            if rn: res.next=ListNode(0)
            res=res.next
        return temp

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        exp, number = 0, 0
        while l1:
            number+=l1.val*(10**exp)
            exp+=1
            l1=l1.next
        exp=0
        while l2:
            number+=l2.val*(10**exp)
            exp+=1
            l2=l2.next
        temp=res=ListNode(0)
        number=str(number)[::-1]
        for i in range(len(number)):
            res.next = ListNode(None) 
            res = res.next
            res.val=int(number[i])
        return temp.next

num1=SinglyLinkedList()
for _ in range(int(input())):
    num1.head=insertNodeAtTail(num1.head, int(input()))
num2=SinglyLinkedList()
for _ in range(int(input())):
    num2.head=insertNodeAtTail(num2.head, int(input()))
s=Solution()
Print(s.addTwoNumbers(num1.head, num2.head))
print()
Print(s.addTwoNumbers1(num1.head, num2.head))
print()
Print(s.addTwoNumbers2(num1.head, num2.head))

"""
4 -> t1
2
4
3
5
3 -> t2
5
6
4
"""