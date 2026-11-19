# Binary Search Tree

class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,new_node):
        if self.root is None:   # Creating the root node
            self.root = new_node
            return  
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left 

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right         

def inorder(temp):  # Recursive
    if temp is None:
        return
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)

btree = BST()
btree.insert(Node(10))
btree.insert(Node(30))
btree.insert(Node(76))
btree.insert(Node(54))
btree.insert(Node(34))

inorder(btree.root)