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
    

#Question 1
import random

def buildRandomTree(root_value, num_nodes):
    print("Question 1")
    if num_nodes <= 0:
        raise ValueError("O número de nós deve ser maior que 0.")

    available_values = list(range(root_value - num_nodes * 2, root_value + num_nodes * 2))
    available_values.remove(root_value)
    random.shuffle(available_values)
    
    values = available_values[:num_nodes - 1]

    bt = BinTree(Node(root_value))

    for value in values:
        bt.insert(value)

    return bt, bt.root

bt, root = buildRandomTree(10, 20)
bt.preOrder(root)
print()
bt.inOrder(root)
print()
bt.postOrder(root)
print()

#Question 2


def findMaxRecursive(node):
    if not node:
        return float('-inf')
    left_max = findMaxRecursive(node.left)
    right_max = findMaxRecursive(node.right)
    return node.data if node.data > left_max else left_max if left_max > right_max else right_max


def findMaxNonRecursive(root):
    if not root:
        return float('-inf')
    max_value = float('-inf')
    stack = [root]
    while stack:
        current = stack.pop()
        if current.data > max_value:
            max_value = current.data
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return max_value

print("\nQuestion 2")

print(findMaxRecursive(root))
print(findMaxNonRecursive(root))

#Question 3


def preorderIterative(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result

def inorderIterative(root):
    result = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    return result

def postorderIterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        current = stack.pop()
        result.append(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return result[::-1]

print("\nQuestion 3")
print(preorderIterative(root))
print(inorderIterative(root))
print(postorderIterative(root))

#Question 4

from collections import deque

def levelOrderTraversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

print("\nQuestion 4")
print(levelOrderTraversal(root))

#Question 5

def searchRecursive(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    elif data < root.data:
        return searchRecursive(root.left, data)
    else:
        return searchRecursive(root.right, data)
    
print("\nQuestion 5")
print(searchRecursive(root, 10))

#Question 6

def sizeRecursive(node):
    if not node:
        return 0
    return 1 + sizeRecursive(node.left) + sizeRecursive(node.right)

def sizeNonRecursive(root):
    if not root:
        return 0
    size = 0
    stack = [root]
    while stack:
        current = stack.pop()
        size += 1
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return size

print("\nQuestion 6")
print(sizeRecursive(root))
print(sizeNonRecursive(root))

#Question 7
from collections import deque

def levelOrderReverseTraversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    stack = []
    
    while queue:
        current = queue.popleft()
        stack.append(current.data)
        
        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)
    
    while stack:
        result.append(stack.pop())
    
    return result


print("\nQuestion 7")
print(levelOrderReverseTraversal(root))


#Question 8

def heightRecursive(node):
    if not node:
        return 0
    left_height = heightRecursive(node.left)
    right_height = heightRecursive(node.right)
    return 1 + max(left_height, right_height)


print("\nQuestion 8")
print(heightRecursive(root))


#Question 9

def maxSumLevel(root):
    if not root:
        return 0, 0  # Nível 0, soma 0
    
    max_sum = float('-inf')
    level = 0
    current_level = 0
    
    queue = deque([(root, 0)])  # (nó, nível)
    
    while queue:
        current_sum = 0
        level_size = len(queue)
        
        for _ in range(level_size):
            current, lvl = queue.popleft()
            current_sum += current.data
            
            if current.left:
                queue.append((current.left, lvl + 1))
            if current.right:
                queue.append((current.right, lvl + 1))
        
        if current_sum > max_sum:
            max_sum = current_sum
            level = current_level
        
        current_level += 1
    
    return level, max_sum


print("\nQuestion 9")
print(maxSumLevel(root))

