#10)

def differentiate_list_and_tuple(data):
    if isinstance(data, list):
        print("It's a list.")
    elif isinstance(data, tuple):
        print("It's a tuple.")
    else:
        print("It's neither a list nor a tuple.")

# Example usage
example_list = [1, 2, 3]
example_tuple = (4, 5, 6)
example_variable = 7

differentiate_list_and_tuple(example_list)
differentiate_list_and_tuple(example_tuple)
differentiate_list_and_tuple(example_variable)
