class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = False

    def setLeft(self, data):
        self.left = Node(data)
        self.isLeft = True

    def setRight(self, data):
        self.right = Node(data)
        self.isLeft = False

class BinTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, root):
        if root is None:
            return
        print(root.data, sep="-->", end="-->")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, sep="-->", end="-->")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep="-->", end="-->")

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if root.left is None:
                root.setLeft(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.setRight(data)
            else:
                self._insert(root.right, data)

    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data < root.data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)
    
    def delete(self, data):
        self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return
        if root.data == data:
            if root.left is None and root.right is None:
                if root.isLeft:
                    root.father.left = None
                else:
                    root.father.right = None
            elif root.left is None:
                if root.isLeft:
                    root.father.left = root.right
                else:
                    root.father.right = root.right
            elif root.right is None:
                if root.isLeft:
                    root.father.left = root.left
                else:
                    root.father.right = root.left
            else:
                tmp = root.right
                while tmp.left is not None:
                    tmp = tmp.left
                root.data = tmp.data
                self._delete(root.right, tmp.data)
        elif data < root.data:
            self._delete(root.left, data)
        else:
            self._delete(root.right, data)
    

