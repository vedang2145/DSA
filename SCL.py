
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    # 2. Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at a specific position (1-based)
    def insert(self,new_node,pos):
        if pos == 1:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        
            
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        new_node = Node(data)

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
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
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)
        else:
            print("List is empty")

    # 5. Delete node by value
    def delete(self):
        data = int(input("Enter value to delete: "))
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    # 6. Reverse linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # 7. Sum of every two consecutive nodes
    def pair_sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next.next

        if temp:
            print("Unpaired node:", temp.data)


# Main program
ll = LinkedList()

while True:
    print("\n--- Singly Linked List Menu ---")
    print("1. Create Linked List")
    print("2. Display Linked List")
    print("3. Insert Node")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum of Consecutive Nodes")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()
    elif choice == 2:
        ll.display()
    elif choice == 3:
        ll.insert()
    elif choice == 4:
        ll.find_middle()
    elif choice == 5:
        ll.delete()
    elif choice == 6:
        ll.reverse()
    elif choice == 7:
        ll.pair_sum()
    elif choice == 8:
        print("Program ended")
        break
    else:
        print("Invalid choice")
