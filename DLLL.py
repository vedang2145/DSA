# Doubly Linear Linked List.

class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self,new_node):
    temp = self.head
    if temp:
      while temp.next:
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp
    else:  # First Node
      self.head = new_node

  def insert(self,new_node,pos):
    temp = self.head 
    if pos == 1:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    else:
      p = 1
      while(p != pos):
        temp = temp.next
        p += 1
      temp.next = new_node
      new_node.prev = temp
      new_node.next = temp.next
      if temp.next:   # This is for last position
        temp.next.prev = new_node  
      temp.next = new_node
      new_node.prev = temp  

  def delete(self,value):
    temp = self.head
    if temp.data == value:
      self.head = self.head.prev
      self.head.prev = None
    else:
      while(temp.data != value and temp):
        temp = temp.next
        if temp == None:
          print("Value is not present in the list")
          return
      temp.prev.next = temp.next
      if temp.next:
        temp.next.prev = temp.prev
      temp = None          

  def print(self):  
    temp = self.head
    print("List elements : ",end=" ")
    while temp:
      print(temp.data,end=" ")
      temp = temp.next  

list1 = LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))   
list1.append(Node(78))
list1.print()
list1.insert(Node(5),1)
list1.print()
list1.delete(102)
list1.print()
  
    