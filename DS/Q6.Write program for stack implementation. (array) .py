
#Q6)stack using array

class Stack:
    #Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 4
        self.top = -1

    #Adds element to the Stack
    def push(self,data):
        if self.top==self.maxSize-1:
            return ("Stack Full!")
        self.top += 1
        self.stack.append(data)
        return True

    #Removes element from the stack
    def pop(self):
        if self.top==-1:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
    #Size of the stack
    def size(self):
        return self.top

s = Stack()
while(True):
    print('p : Push')
    print('o : Pop')
    print('e : Exit')
    ch = input('Eneter ur choice')
    if ch == 'e':
        break
    if ch == 'p':
        i= int(input('Enter an element to be pushed in stack'))
        print(s.push(i))#prints True
    if ch == 'o':
        print(s.pop())
