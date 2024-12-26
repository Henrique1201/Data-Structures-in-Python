def linked_list():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            if self.head is None:
                self.head = Node(data)
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

        def prepend(self, data):
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head

        def delete(self, data):
            if self.head is None:
                return
            if self.head.data == data:
                self.head = self.head.next
                return
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

        def __str__(self):
            current = self.head
            ret = ''
            while current:
                ret += str(current.data) + ' '
                current = current.next
            return ret

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.prepend(0)
    ll.delete(2)
    print(ll)

linked_list()