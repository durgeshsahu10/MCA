
import math
#function to calculate the midpoints of grouped data.
def calculate_midpoints(classes):
    midpoints = []
    for class_range in classes:
        lower,upper = class_range
        midpoint = (lower+upper)/2
        midpoints.append(midpoint)
    return midpoints

#function to calculate the mean of grouped data.
def calculate_mean(midpoints, frequencies):
    sum_product = sum(midpoints[i]* frequencies[i] for i in range(len(midpoints)))
    total_frequency = sum(frequencies)
    mean = sum_product / total_frequency
    return mean
#function to calculate the standard deviation of grouped data.
def calculate_standard_deviation(midpoints, frequencies, mean):
    sum_squarred_diff = sum(frequencies[i] * (midpoints[i] - mean) ** 2 for i in range(len(midpoints)))
    total_frequency = sum(frequencies)
    variance = sum_squarred_diff / total_frequency
    std_deviation = math.sqrt(variance)
    return std_deviation

#Example groped data(class ranges and frequencies)
class_ranges = [(10,20), (20,30), (30,40), (40,50)]
frequencies = [5,8,12,7]

#calculate midpoints, mean and standard deviation.
midpoints = calculate_midpoints(class_ranges)
mean = calculate_mean(midpoints, frequencies)
std_deviation = calculate_standard_deviation(midpoints, frequencies, mean)
#output the results print("Grouped data")
for i in range(len(class_ranges)):
    lower, upper = class_ranges[i]
    print(f"{lower} - {upper} Frequency: {frequencies[i]}")
print("\nMean: ",mean)
print("Standard deviation:", std_deviation)
