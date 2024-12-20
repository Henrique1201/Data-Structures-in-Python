class Node:
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev
    
    # Getters
    @property
    def data(self):
        return self._data
    
    @property
    def next(self):
        return self._next
    
    @property
    def prev(self):
        return self._prev
    
    # Setters
    @data.setter
    def data(self, data):
        self._data = data
    
    @next.setter
    def next(self, next):
        self._next = next
    
    @prev.setter
    def prev(self, prev):
        self._prev = prev
    
    def __str__(self):
        return "Node[Data=%s]" % self.data


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enQueue(self, data):
        n = Node(data)
        if self.size == 0:
            self.front = self.rear = n
        else:
            self.rear.next = n
            n.prev = self.rear
            self.rear = n
        self.size += 1
    
    def deQueue(self):
        if self.size == 0:
            raise IndexError("Queue is empty. Cannot dequeue.")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        self.size -= 1
        return data
    
    def get_front(self):
        if self.size == 0:
            raise IndexError("Queue is empty. No front element.")
        return self.front.data
    
    def get_rear(self):
        if self.size == 0:
            raise IndexError("Queue is empty. No rear element.")
        return self.rear.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)


# Question 1: Reverse queue using stack
def reverse_queue_using_stack(queue):
    stack = []
    
    while len(queue) > 0:  # Removendo todos os elementos da fila para a pilha
        stack.append(queue.deQueue())
    
    while stack:  # Reenfileirando os elementos na ordem inversa
        queue.enQueue(stack.pop())
    
    return queue


print("\nQuestion 1")
queue = Queue()
for i in range(1, 6):
    queue.enQueue(i)
print("Original queue:", queue)
reverse_queue_using_stack(queue)
print("Reversed queue:", queue)


# Question 2: Reverse first k elements of a queue
def reverse_first_k_elements(queue, k):
    if k > len(queue):
        raise ValueError("k cannot be greater than the size of the queue.")
    
    stack = []
    for _ in range(k):
        stack.append(queue.deQueue())
    
    while stack:
        queue.enQueue(stack.pop())
    
    size = len(queue)
    for _ in range(size - k):
        queue.enQueue(queue.deQueue())
    
    return queue


print("\nQuestion 2")
queue = Queue()
for i in range(1, 6):
    queue.enQueue(i)
print("Original queue:", queue)
reverse_first_k_elements(queue, 3)
print("Reversed first 3 elements:", queue)


# Question 3: Queue using two stacks
class QueueUsingTwoStacks:
    def __init__(self):
        self.S1 = []  # Primary stack for enqueue operations
        self.S2 = []  # Auxiliary stack for dequeue operations
    
    def enQueue(self, data):
        self.S1.append(data)
    
    def deQueue(self):
        if not self.S2:  # If S2 is empty
            if not self.S1:  # If S1 is also empty
                raise IndexError("Queue is empty. Cannot dequeue.")
            while self.S1:
                self.S2.append(self.S1.pop())
        return self.S2.pop()


print("\nQuestion 3")
queue = QueueUsingTwoStacks()
for i in range(1, 6):
    queue.enQueue(i)
print("Dequeued:", queue.deQueue())
queue.enQueue(6)
print("Dequeued:", queue.deQueue())
