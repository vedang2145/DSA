# 1.Create

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

a = Node(5)
b = Node(3)
c = Node(7)

a.next = b
b.next = c

head = a

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# 2.Traversing

def linkedList(head):
  curr = head

  while curr != None:
    print(curr.data, end=" ")
    curr = curr.next

# linkedList(head)

# 3.Insertion at Beginning

newNode = Node(4)
newNode.next = head
head = newNode

linkedList(head)

