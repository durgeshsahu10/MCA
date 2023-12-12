def find_range(numbers):
    if len(numbers) == 0:
       return None
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return range_val
numbers = [4,9,2,15,6,12]
result = find_range(numbers)
if result is not None:
   print(f"The range of the numbers is: {result}") 
else:
   print(f"The list is empty,so there is no range.")

