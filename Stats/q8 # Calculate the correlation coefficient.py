#8)
import numpy as np

def calculate_correlation(x_values, y_values):
    # Calculate the correlation coefficient
    correlation_coefficient = np.corrcoef(x_values, y_values)[0, 1]
    return correlation_coefficient

# Example usage
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 3, 5]

correlation_result = calculate_correlation(x_data, y_data)
print(f"The correlation coefficient is: {correlation_result:.4f}")