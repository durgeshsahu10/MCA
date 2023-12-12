#Name: Durgesh Sahu.
#Q3)Program to create Doubly Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return

        data = int(input("Enter the data for node 1: "))
        new_node = Node(data)
        self.head = new_node

        for i in range(1, n):
            data = int(input(f"Enter the data for node {i+1}: "))
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_begin(self):

        if not self.head:
            print("List is empty!")
            return

        data = int(input("Enter the data to insert at the beginning: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_end(self):
        if not self.head:
            print("List is empty!")
            return

        data = int(input("Enter the data to insert at the end: "))
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_middle(self):
        if not self.head:
            print("List is empty!")
            return

        data = int(input("Enter the data to insert: "))
        pos = int(input("Enter the position to insert at: "))
        new_node = Node(data)

        current = self.head
        count = 1
        while count < pos - 1:
            current = current.next
            count += 1
        
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    def delete(self):
        if not self.head:
            print("List is empty!")
            return

        data = int(input("Enter the data to delete: "))
        current = self.head

        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current.next = None
            print("Node deleted!")
            return
        
        while current.next:
            if current.data == data:
                break   
            current = current.next
        
        if current.data != data:
            print("Node not found!")
            return
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        current.prev = None
        current.next = None
        print("Node deleted!")

    def search(self):
        if not self.head:
            print("List is empty!")
            return
        data = int(input("Enter the data to search: "))
        current = self.head
        count = 1
        while current:
            if current.data == data:
                print(f"Node found at position {count}")
                return
            current = current.next
            count += 1
        print("Node not found!")
    
    def sort(self):
        if not self.head:
            print("List is empty!")
            return
        current = self.head
        while current:
            temp = current.next
            while temp:
                if current.data > temp.data:
                    current.data, temp.data = temp.data, current.data   
                temp = temp.next
            current = current.next

        print("List sorted!")

    def modify(self):
        if not self.head:
            print("List is empty!")
            return
        
        data = int(input("Enter the data to modify: "))
        new_data = int(input("Enter the new data: "))
        current = self.head
        while current:
            if current.data == data:
                current.data = new_data
                print("Node modified!")
                return  
            current = current.next
        print("Node not found!")

    def reverse(self):
        if not self.head:
            print("List is empty!")
            return

        current = self.head
        while current.next:
            current.next, current.prev = current.prev, current.next
            current = current.prev

        current.next, current.prev = current.prev, current.next
        self.head = current
    print("List reversed!")

    def display(self):
        if not self.head:
            print("List is empty!")
            return
        curr = self.head
        while curr:
            print(curr.data,end='<->')
            curr = curr.next    
        print('None')

# Main Program

dll = DoublyLinkedList()

while True:

    print("***** Doubly Linked List Menu *****")
    print("1. Create a list")
    print("2. Insert at the beginning")
    print("3. Insert at the end")
    print("4. Insert at a middle position")
    print("5. Delete a node")
    print("6. Search for a node")
    print("7. Sort the list")
    print("8. Modify a node")
    print("9. Reverse the list")
    print("10. Display the list")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()
    elif choice == 2:
        dll.insert_begin()
    elif choice == 3:
        dll.insert_end()
    elif choice == 4:
        dll.insert_middle()
    elif choice == 5:
        dll.delete()
    elif choice == 6:
        dll.search()
    elif choice == 7:
        dll.sort()
    elif choice == 8:
        dll.modify()
    elif choice == 9:
        dll.reverse()
    elif choice == 10:
        dll.display()
    elif choice == 11:
        break
    else:   
        print("Invalid choice! Please enter a number between 1 and 11.")