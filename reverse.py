# Print node values in reverse order
# in Doubly Linear Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print_forward(self):
        temp = self.head
        print("Forward order:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def print_reverse(self):
        temp = self.head

        # Move to the last node
        while temp and temp.next:
            temp = temp.next

        print("Reverse order:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(78))

list1.print_forward()
list1.print_reverse()