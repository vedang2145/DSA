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

    def delfirst_last(self):
        if self.head is None:
            print("Linked List is empty")
            return

        

        # Delete first node
        self.head = self.head.next

        # If list became empty
        if self.head is None:
            return

        # Delete last node
        temp = self.head
        prev = None

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None


# Main program
ll = LinkedList()

ll.create(10)
ll.create(20)
ll.create(30)
ll.create(40)
ll.create(50)

print("Original Linked List:")
ll.display()

ll.delfirst_last()

print("After deleting first and last nodes:")
ll.display()