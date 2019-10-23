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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.val==
        while :
        	pass


s= Solution()
Li= SinglyLinkedList()
Li_head =insertNodeAtTail(Li.head, 4)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 5)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 1)
Li.head =Li_head
Li_head =insertNodeAtTail(Li.head, 9)
Li.head =Li_head
Li_head = s.deleteNode(Li.head, 5)
Li.head = Li_head
Print(Li_head)
