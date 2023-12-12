
#Q1) Write a Program for implementation of array operations.

#Create an Array
b=[2,15,3,4,25,50,43,45,45,34,23]

#1)Accessing Array Elements
for i in range(1,6):
    print(b[i])

#2)sort the array
b.sort()
print("After sorting:-",b)

#3)reverse
b.reverse()
print("Reverse:-",b)

#4)removeing elements
b.remove(50)
print("Remove:-",b)

#5)Insert
b.insert(0,100)
print("Insert:-",b)

#6)Append
b.append(101)
print("Append:-",b)

#7)Extend
b.extend([200,210])
print("Extend:-",b)

#8)Slicing
A=b[1:3]
print("slicing:-",A)

#9)Length
length=len(b)
print("length of an Array:-",length)

#10)Count
total=b.count(45)
print("Total:-",total)
