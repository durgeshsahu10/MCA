# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:03:09 2023

@author: Pratham
"""

#Q17)Binary Search
def bin_search(arr, key):
    low = 0
    high = len(arr)-1
    while low<= high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid -1
    return -1
arr1 = []
while(True):
    str = input('Enter array ele and enter done when finished')
    if str == 'done':
        break
    else:
        arr1.append(int(str))
print('Entered array:')
print(arr1)
k = int (input('Enter element to be searched in list'))
find = bin_search(arr1, k)
if find == -1:
    print('Element not found')
else:
    print('%d found at location %d' % (k, find+1))