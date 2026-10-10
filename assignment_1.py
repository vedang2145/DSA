
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            value = int(input("Enter node value: "))
            self.insert_end(value)

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and print
    def traverse(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at a specific position
    def insert_position(self, value, position):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(value)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find middle node
    def middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete a node by value
    def delete(self, value):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
            print("Node deleted")
            return

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
            return

        temp.next = temp.next.next
        print("Node deleted")

    # 6. Reverse Linked List
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        print("List reversed")

    # 7. Sum of every two consecutive nodes
    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Main program
ll = LinkedList()

while True:
    print("\n1. Create Linked List")
    print("2. Traverse")
    print("3. Insert at Position")
    print("4. Find Middle")
    print("5. Delete Node")
    print("6. Reverse List")
    print("7. Sum Consecutive Nodes")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()
    elif choice == 2:
        ll.traverse()
    elif choice == 3:
        value = int(input("Enter value: "))
        position = int(input("Enter position: "))
        ll.insert_position(value, position)
    elif choice == 4:
        ll.middle()
    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete(value)
    elif choice == 6:
        ll.reverse()
    elif choice == 7:
        ll.consecutive_sum()
    elif choice == 8:
        break
    else:
        print("Invalid choice")
