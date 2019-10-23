"""
class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.insert(0,item)

  def pop(self):
    return self.items.pop(0)

  def top(self):
    return self.items[0]

  def size(self):
    return len(self.items)

s = Stack()
t = head
t2 = head
while t != None:
  s.push(t.data)
  t = t.next
while head!=None:
  head.data = s.pop()
  head = head.next
return t2
"""

class Node:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

def Print(node):
  while node:
    print(node.data,end=' ')
    node = node.next

def insertNodeAtTail(head, data):
    temp = Node(data)
    if head==None:
      head = temp
      return head
    temp2 = head
    while temp2.next:
      temp2 = temp2.next
    temp2.next = temp
    return head


class Solution:
  def reverseList(self, head: Node) -> Node:
    a=head
    r=None
    while a != None:
      t = a.next
      a.next = r
      r = a
      a = t
    return r


s= Solution()
Li= SinglyLinkedList()
Li_head =insertNodeAtTail(Li.head, 1)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 2)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 3)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 4)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 5)
Li.head =Li_head
Li_head = s.reverseList(Li.head)
Li.head = Li_head
Print(Li_head)
