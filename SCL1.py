
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

    # 2. Display linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    # 3. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    # 4. Insert at end
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # 5. Delete first node
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            self.head = self.head.next
            temp.next = self.head

    # 6. Delete last node
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head

    # 7. Search a value
    def search(self):
        data = int(input("Enter value to search: "))

        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == data:
                print("Value found")
                return

            temp = temp.next

            if temp == self.head:
                break

        print("Value not found")


# Main program
cll = CircularLinkedList()

while True:
    print("\n--- Singly Circular Linked List ---")
    print("1. Create")
    print("2. Display")
    print("3. Insert at Beginning")
    print("4. Insert at End")
    print("5. Delete Beginning")
    print("6. Delete End")
    print("7. Search")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()
    elif choice == 2:
        cll.display()
    elif choice == 3:
        cll.insert_beginning()
    elif choice == 4:
        cll.insert_end()
    elif choice == 5:
        cll.delete_beginning()
    elif choice == 6:
        cll.delete_end()
    elif choice == 7:
        cll.search()
    elif choice == 8:
        print("Program ended")
        break
    else:
        print("Invalid choice")
