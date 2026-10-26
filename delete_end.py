class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

current = head

while current.next.next is not None:
  current = current.next
  print(current)
current.next = None  

current = head

while current is not None:
  print(current.data,end="->")
  current = current.next
print("None")  