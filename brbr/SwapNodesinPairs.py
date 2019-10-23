class Node:
  def __init__(self, node_val):
    self.val = node_val
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

def Print(node):
  while node:
    print(node.val,end=' ')
    node = node.next

def insertNodeAtTail(head, val):
    temp = Node(val)
    if head==None:
      head = temp
      return head
    temp2 = head
    while temp2.next:
      temp2 = temp2.next
    temp2.next = temp
    return head

class Solution:
    def swapPairs(self, head: Node) -> Node:
        if not head or not head.next: return head #sirve para retornar si el numero de elementos es impar el elemento que sobra
        second = head.next
        head.next = self.swapPairs(head.next.next)
        second.next=head
        return second

    def iterative(self, head: Node) -> Node:
    	t = head
    	while head and head.next:
    		head.val, head.next.val = head.next.val, head.val
    		head = head.next.next
    	return t

s= Solution()
Li= SinglyLinkedList()
for i in range(int(input())):
	a=int(input())
	Li_head =insertNodeAtTail(Li.head, a)
	Li.head =Li_head
Li.head=s.iterative(Li.head)
Print(Li.head)