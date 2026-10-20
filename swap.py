# Write a function to swap first & last node in DLL.

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None

def swap(head):
  if head is None or head.next is None:
    return head

  temp = head
  while temp.next is not None:
    temp = temp.next  

  head.data, temp.data = temp.data, head.data

  return head

def display(head):
  temp = head
  while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next

head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

print("Before Swapping : ")  
display(head)

head = swap(head)

print("\nAfter Swapping :" )
display(head)
    