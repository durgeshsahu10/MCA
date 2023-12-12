# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:41:22 2023

@author: Pratham
"""

#Q13)program for queue implementation using array
class Queue:
    #Constructor
    def __init__(self, c):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = c
    #Adds element to the queue
    def Enqueue(self,data):
        if self.rear>=self.capacity-1:
            return ("Queue is Full!")
        self.rear += 1
        self.queue.append(data)
        return True
    #Removes element from the queue
    def Dequeue(self):
        if self.front == self.rear + 1:
            return ("Queue Empty!")
        item = self.queue[self.front]
        self.front += 1
        return item
q = Queue(4)
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