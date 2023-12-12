# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:31:58 2023

@author: Pratham
"""

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
def reverse_string(string):
    stack = Stack()
# Push each character of the string into the stack
    for character in string:
        stack.push(character)
# Pop each character from the stack to get the reversed string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
# Test the program
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
