class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def delete(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:  # Only one element
                    self.head = None
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                curr = self.head
                while curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == key:
                        prev.next = curr.next
                        curr = curr.next

    def traverse(self):
        if self.head:
            temp = self.head
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print()

    def search(self, key):
        if self.head:
            temp = self.head
            while True:
                if temp.data == key:
                    return True
                temp = temp.next
                if temp == self.head:
                    break
        return False

# Example usage:
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.traverse()  # Output: 0 -> 1 -> 2 -> 3 -> 
print(cll.search(2))  # Output: True
print(cll.search(4))  # Output: False
cll.delete(2)
cll.traverse()  # Output: 0 -> 1 -> 3 -> 
cll.delete(0)
cll.traverse()  # Output: 1 -> 3 -> 