
#Q4)circular singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the end of the list
    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head

    # Deletion by key
    def delete(self, key):
        if not self.head:   
            print("List is empty.")
            return
        elif self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
        else:
            prev = self.head
            curr = self.head.next
            while curr != self.head:
                if curr.data == key:
                    prev.next = curr.next
                    return  
                prev = curr
                curr = curr.next
            print("Key not found.")

    # Display the circular linked list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head    
        while True:
            print(curr.data, end="<->")
            curr = curr.next
            if curr == self.head:
                break
        print()

# Menu-driven program
clist = CircularLinkedList()
while True:
    print("\nCircular Linked List Operations")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Display the list")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the element to be inserted: "))
        clist.insert(data)
        print("Element", data, "inserted successfully.")
    elif choice == 2:
        key = int(input("Enter the element to be deleted: "))
        clist.delete(key)
    elif choice == 3:   
        print("Circular linked list:")
        clist.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")