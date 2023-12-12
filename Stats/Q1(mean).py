def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0
    else:
        total = sum(numbers)
        mean = total/len(numbers)
        return mean

numbers = [45,27,63,12,45,78,34,27,56,89,45,27,12,34,56,78]
mean = calculate_mean(numbers)
print("Mean: ", mean)
