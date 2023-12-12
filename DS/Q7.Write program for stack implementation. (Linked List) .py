##Name: Durgesh Sahu.
#Q7)stack using Linked List
class Node:
    
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # top is default NULL
    def __init__(self):
        self.top = None

    # Checks if stack is empty
        def isempty(self):
            if self.top == None:
                return True
            else:
                return False

    # Method to add data to the stack
    # adds to the start of the stack

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
        else:
            new1 = Node(data)
            new1.next = self.top
            self.top = new1
  
    # Remove element that is the current top (start of the stack)
    def pop(self):
        if self.isempty():
            return ("stack empty")
        else:   
            # Removes the top node and makes
            # the preceding one the new top
            curr = self.top
            self.top = self.top.next
            curr.next = None
            return curr.data

MyStack = Stack()
while(True):
    print('p : Push')
    print('o : Pop')    
    print('e : Exit')
    ch = input('Eneter ur choice')  
    if ch == 'e':
        break   
    if ch == 'p':
        i= int(input('Enter an element to be pushed in stack'))
        MyStack.push(i)
    if ch == 'o':
        print(MyStack.pop())
        
