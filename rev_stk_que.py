
# W.A.P to reverse stack elements using queue.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    def display(self):
        temp = self.top
        print("Stack Elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new = Node(data)

        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front is None:
            return None

        temp = self.front
        data = temp.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def display_queue(self):
        curr = self.front
        print("Queue Elements:")
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


def reverse_stack(st1):
    q1 = Queue()

    # Transfer Stack to Queue
    while st1.top is not None:
        q1.enqueue(st1.pop())

    q1.display_queue()

    # Transfer Queue back to Stack
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))


def reverse_queue(st2):
    s1 = Stack()

    # Transfer Queue to Stack
    while not st2.is_empty():
        s1.push(Node(st2.dequeue()))

    # Transfer Stack back to Queue
    while s1.top is not None:
        st2.enqueue(s1.pop())


# Main Program
st = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))

print("Original Stack:")
st.display()

reverse_stack(st)

print("\nReversed Stack:")
st.display()
