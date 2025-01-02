class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node_data, data):
        new_node = Node(data)
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current is None:
            print("The previous node is not in the list.")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("The key is not present in the list.")
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_beginning(0)
    sll.insert_after(1, 1.5)
    print("List after insertions:", sll.traverse())

    sll.delete_node(1.5)
    print("List after deleting 1.5:", sll.traverse())

    print("Searching for 2:", sll.search(2))
    print("Searching for 3:", sll.search(3))