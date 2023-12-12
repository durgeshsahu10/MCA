# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:05:17 2023

@author: Pratham
"""

#Q18)Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n): #passes = n-1
        for j in range(0, n-1-i): #comparisions = n-1-i
            if (arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [12,34,45,6, 8, 9,-10]
print('Before sorting',arr)
bubble_sort(arr)
print('Sorted arr',arr)