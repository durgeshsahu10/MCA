def calculate_median(numbers):
    #sort the list of numbers
    numbers.sort()
    #find the length of the list
    n=len(numbers)
    #check if the list is empty
    if n==0:
        return None
    #check if the list an odd or even no of elements
    if n%2==1:
        #if the list has an odd no of elements,return the middle element return number[n//2]
        return numbers[n//2]
    else:
        #if the list has an even no of elements ,return the average of the two middle elements
        middle1=numbers[n//2-1]
        middle2=numbers[n//2]
        return(middle1+middle2)/2
#creating an empty list
numbers=[]
#number of elements as input
n=int(input("Enter no of elemets:"))
#iterating till the range
for i in range(0,n):
    ele=int(input())
    #adding the element
    numbers.append(ele)
print(numbers)
median=calculate_median(numbers)
print("Median",median)

