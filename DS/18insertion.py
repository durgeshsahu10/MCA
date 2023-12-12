# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:06:58 2023

@author: Pratham
"""

#Q18)Insertiom Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# Main program
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Original array:", numbers)
insertion_sort(numbers)
print("Sorted array:", numbers)