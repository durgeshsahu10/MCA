# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 10:00:12 2023

@author: Pratham
"""

#Q17)Linear search
def l_search(arr, key):
    flag = False
    n= len(arr)
    for i in range(n):
        if arr[i] == key:
            print('%d found at location %d' %(key, i+1))
            flag = True
            break
    if i == n-1 and flag == False:
        print('Element not in list')
arr1 = []
while(True):
    str = input('Enter array ele and enter done when finished')
    if str == 'done':
        break
    else:
        arr1.append(int(str))
print('Entered array:')
print(arr1)
k = int (input('Enter elemet to be searched in list'))
l_search(arr1, k)