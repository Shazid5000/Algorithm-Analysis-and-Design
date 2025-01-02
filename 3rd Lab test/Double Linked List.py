class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_after(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current is None:
            print("The previous node is not in the list.")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_node(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            print("The key is not present in the list.")
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        if temp == self.head:
            self.head = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def traverse_backward(self):
        elements = []
        current = self.head
        if current is None:
            return elements
        while current.next:
            current = current.next
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_beginning(0)
    dll.insert_after(1, 1.5)
    print("List after insertions:", dll.traverse_forward())

    dll.delete_node(1.5)
    print("List after deleting 1.5:", dll.traverse_forward())

    print("Searching for 2:", dll.search(2))
    print("Searching for 3:", dll.search(3))

    print("Traverse backward:", dll.traverse_backward())