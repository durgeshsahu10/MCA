#Q11)program to check inout string is palindrome or not
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def is_palindrome(string):
        stack = Stack()
        for char in string:
            stack.push(char)
        reverse_string = ""
        while not stack.is_empty():
            reverse_string += stack.pop()
        return string == reverse_string
# Test the program
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(input_string, "is a palindrome.")
else:
    print(input_string, "is not a palindrome.")