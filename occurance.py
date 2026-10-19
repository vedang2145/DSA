class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def countOccurrence(head, num):
    count = 0
    temp = head

    while temp is not None:
        if temp.data == num:
            count += 1
        temp = temp.next

    return count

# Creating a doubly linked list
head = Node(10)
second = Node(20)
third = Node(10)
fourth = Node(30)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

num = 10
print("Occurrence:", countOccurrence(head, num))