
#Q2)Program to create Singly Linked List.

class Node:
    
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_at_middle(self, data, position):
        new_node = Node(data)
        curr_node = self.head
        for _ in range(1, position):
            if curr_node is None:
                print("Position out of range")
                return
            curr_node = curr_node.next
        new_node.next = curr_node.next
        curr_node.next = new_node

    def delete_node(self, data):
        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        while curr_node and curr_node.data != data:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            print("Data not found.")
            return

        prev.next = curr_node.next
        curr_node = None

    def search_node(self, data):
        curr_node = self.head
        position = 1
        while curr_node:
            if curr_node.data == data:
                print(f"Data found at position {position}")
                return
            curr_node = curr_node.next 
            position += 1
        print("Data not found.")

    def sort_list(self):
        curr_node = self.head
        elements = []
        while curr_node:
            elements.append(curr_node.data)
            curr_node = curr_node.next
        elements.sort()
        self.head = None
        for element in elements:
            self.insert_at_end(element)

    def modify_node(self, old_data, new_data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == old_data:
                curr_node.data = new_data
                return
            curr_node = curr_node.next
        print("Data not found.")

    def reverse_list(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
    
    def display_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

linked_list = LinkedList()

while True:
    print("1. Create a singly linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at middle")
    print("5. Delete a node")
    print("6. Search a node")
    print("7. Sort the list")
    print("8. Modify a node")
    print("9. Reverse the list")
    print("10. Display the list")
    print("11. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number of elements: "))
        for _ in range(n):
            data = int(input("Enter element: "))    
            linked_list.insert_at_end(data)
        print("Linked list created successfully.")

    elif choice == 2:
        data = int(input("Enter element to insert at beginning: "))
        linked_list.insert_at_beginning(data)
        print("Element inserted successfully.")

    elif choice == 3:
        data = int(input("Enter element to insert at end: "))
        linked_list.insert_at_end(data)
        print("Element inserted successfully.")

    elif choice == 4:   
        data = int(input("Enter element to insert: "))
        position = int(input("Enter position to insert at: "))
        linked_list.insert_at_middle(data, position)
        print("Element inserted successfully.")

    elif choice == 5:
        data = int(input("Enter element to delete: "))
        linked_list.delete_node(data)
        print("Element deleted successfully.")

    elif choice == 6:
        data = int(input("Enter element to search: "))
        linked_list.search_node(data)

    elif choice == 7:   
        linked_list.sort_list()
        print("List sorted successfully.")

    elif choice == 8:
        old_data = int(input("Enter data to modify: "))
        new_data = int(input("Enter new data: "))
        linked_list.modify_node(old_data, new_data) 
        print("Node modified successfully.")
    
    elif choice == 9:
        linked_list.reverse_list()
        print("List reversed successfully.")

    elif choice == 10:
        print("Linked List: ", end="")
        linked_list.display_list()

    elif choice == 11:
        break
    
    else:
        print("Invalid choice! Please try again.")

    print()

print("Exiting...")
