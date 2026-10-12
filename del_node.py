class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def findmid_del(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = temp1 = self.head
        prev = None

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle Node:", temp.data)

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

        temp = None


# Main program
ll = LinkedList()

ll.create(10)
ll.create(20)
ll.create(30)
ll.create(40)
ll.create(50)

print("Original Linked List:")
ll.display()

ll.findmid_del()

print("After deleting middle node:")
ll.display()

ll.reverse()

print("After reversing:")
ll.display()