class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def del_alternate(self):
        prev = self.head

        if prev is None:
            return

        temp = self.head.next

        while prev and temp:
            prev.next = temp.next
            temp = None
            prev = prev.next

            if prev:
                temp = prev.next


# Main program
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)

print("Original Linked List:")
ll.traverse()

ll.del_alternate()

print("After deleting alternate nodes:")
ll.traverse()