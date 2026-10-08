# Delete a node from a singly linked list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def delete_node(self, value):
        temp = self.head
        prev = None

        # If the list is empty
        if temp is None:
            print("List is empty")
            return

        # Delete the head node
        if temp.data == value:
            self.head = temp.next
            return

        # Find the node to delete
        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next

        # Value not found
        if temp is None:
            print("Value not found in the list")
            return

        # Remove the node
        prev.next = temp.next


# Create linked list
linked_list = LinkedList()

linked_list.append(Node(10))
linked_list.append(Node(20))
linked_list.append(Node(30))
linked_list.append(Node(40))

print("Original List:")
linked_list.print_list()

linked_list.delete_node(30)
print("After deleting 30:")
linked_list.print_list()

linked_list.delete_node(10)
print("After deleting 10:")
linked_list.print_list()

linked_list.delete_node(100)