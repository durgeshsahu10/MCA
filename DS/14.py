# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:46:08 2023

@author: Pratham
"""

#Q14)program for queue implementation using linked list
class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    # top is default NULL
    def __init__(self):
        self.front = None
        self.rear = None
    # Method to add data to the stack
    # adds to the start of the stack
    def Add(self, data):
            if self.front == None:
                self.front = Node(data)
                self.rear = self.front
            else:
                new1 = Node(data)
                self.rear.next = new1
                self.rear = new1
    # Remove element that is the current top (start of the stack)
    def delete(self):
        if self.front == None:
            return ("Queue Empty!")
        else:
                # Removes the top node and makes
                # the preceding one the new top
                curr = self.front
                self.front = self.front.next
                curr.next = None
                return curr.data
My_q = Queue()
while(True):
    print('a : add')
    print('d : delete')
    print('e : Exit')
    ch = input('Eneter ur choice')
    if ch == 'e':
        break
    if ch == 'a':
        i= int(input('Enter an element to be pushed in stack'))
        My_q.Add(i)
    if ch == 'd':
        print(My_q.delete())