class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.rec_insert(self.root,data)

    def rec_insert(self,root,data):

        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.rec_insert(root.left,data)
        else:
            root.right = self.rec_insert(root.right,data)

        return root

    def inorder(self):
        self.rec_inorder(self.root)

    def rec_inorder(self,root):
        if root:
            self.rec_inorder(root.left)
            print(root.data,end=" ")
            self.rec_inorder(root.right)
    def min(self,root):
        while root.left:
            root = root.left
        return root.data

    def max(self,root):
        while root.right:
            root = root.right
        return root.data

    def search(self,root,key):
        if root is None:
            return root
        if  root.data == key:
                return root
        if root.data>key:
            return self.search(root.left,key)
        return self.search(root.right,key)





obj = BST()
obj.insert(9)
obj.insert(4)
obj.insert(2)
obj.insert(5)
obj.insert(10)
obj.insert(15)
obj.insert(13)
obj.inorder()
print()
print( obj.search(obj.root , 15).data  )
