# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:16:10 2023

@author: Pratham
"""

#Q20)Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swap elements
        heapify(arr, n, largest)
# Function to perform heap sort
def heapSort(arr):
    n = len(arr)
    # Building max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extracting elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap elements
        heapify(arr, i, 0)
# Get user input for the array
arr = input("Enter elements of the array separated by space: ").split()
arr = [int(num) for num in arr]
print("Input array:", arr)
heapSort(arr)
print("Sorted array:", arr)