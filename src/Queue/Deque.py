class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"Node({self.data})"


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def addFront(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def addRear(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def removeFront(self):
        if self.size == 0:
            raise IndexError("Deque is empty. Cannot remove from front.")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self.size -= 1
        return data

    def removeRear(self):
        if self.size == 0:
            raise IndexError("Deque is empty. Cannot remove from rear.")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        self.size -= 1
        return data

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return " <-> ".join(result)


deque = Deque()

deque.addFront(10)
deque.addRear(20)
deque.addFront(5)
deque.addRear(25)

print("Deque após adicionar elementos:")
print(deque)

print("\nRemovendo da frente:", deque.removeFront())
print("Removendo do final:", deque.removeRear())

print("\nDeque após remoções:")
print(deque)

print("\nTamanho do deque:", len(deque))
print("Deque está vazio?", deque.isEmpty())
