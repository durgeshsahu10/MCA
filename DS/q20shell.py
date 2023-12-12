# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:14:15 2023

@author: Pratham
"""

#Q20)Shell Sort
def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
# Taking input from the user
arr = list(map(int, input("Enter the elements of the array: ").split()))
print("Original array:")
print(arr)
shellSort(arr)
print("Sorted array:")
print(arr)
