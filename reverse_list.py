# Reversing a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse link
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        self.head = prev              # Update head


# Create linked list
ll = LinkedList()
ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))
ll.append(Node(40))

print("Original List:")
ll.print_list()

ll.reverse()

print("Reversed List:")
ll.print_list()