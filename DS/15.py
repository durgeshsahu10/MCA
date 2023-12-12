# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:50:38 2023

@author: Pratham
"""

#Q15) program for circular queue using array
class Queue:
    #Constructor
    def __init__(self, c):
        self.front = 0
        self.rear = -1
        self.capacity = c
        self.cnt = 0
        self.queue = [None] *self.capacity
    #Adds element to the queue
    def Enqueue(self,data):
        if self.cnt ==self.capacity:
            return ("Queue is Full!")
        self.rear = (self.rear +1) % self.capacity
        self.queue[self.rear] = data
        self.cnt += 1
        return True
    #Removes element from the queue
    def Dequeue(self):
        if self.cnt == 0:
            return ("Queue Empty!")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.cnt -= 1
        return item
q = Queue(3)
while(True):
    print('a : Add')
    print('d : Delete')
    print('e : Exit')
    ch = input('Eneter ur choice')
    if ch == 'e':
        break
    if ch == 'a':
        i= int(input('Enter an element to be added in queue'))
        print(q.Enqueue(i))#prints True
    if ch == 'd':
        print(q.Dequeue())