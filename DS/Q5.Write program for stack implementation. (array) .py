
# Q5)circular doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    # Add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.prev = last_node
            new_node.next = self.head
            self.head.prev = new_node
 
    # Display the circular doubly linked list
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while True:
                print(current.data, end='<->')
                current = current.next
                if current == self.head:
                    break
            print()

# Create a circular doubly linked list and perform operations
cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(4)
cdll.append(5)
# Display the circular doubly linked list
cdll.display()
