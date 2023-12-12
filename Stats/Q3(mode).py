
def calculate_mode(numbers):
   # Create a dictionary to store the count of each number
   count_dict = {}

   # Count the frequency of each number in the list
   for num in numbers:
       if num in count_dict:
          count_dict[num] += 1
       else:
          count_dict[num] = 1
   # Find the maximum count
   max_count = max(count_dict.values())
   # find the numbers with the maximum count (the mode)
   mode = [num for num, count in count_dict.items() if count == max_count]
   return mode

# creating an empty list
numbers = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    numbers.append(ele)
print(numbers)
mode_result = calculate_mode(numbers)
print("Mode:", mode_result)
