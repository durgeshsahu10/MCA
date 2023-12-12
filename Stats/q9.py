#9) 
import math

def binomial_probability(n, k, p):
    """
    Calculate the probability of getting exactly k successes in n trials
    with a probability of success p on a single trial.
    """
    # Calculate binomial coefficient
    binomial_coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    
    # Calculate probability using the binomial distribution formula
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    
    return probability

# Example usage
n_trials = 5  # number of trials
k_successes = 2  # number of successful outcomes
probability_of_success = 0.3  # probability of success on a single trial

result = binomial_probability(n_trials, k_successes, probability_of_success)
print(f"The probability of getting exactly {k_successes} successes in {n_trials} trials is: {result:.4f}")
