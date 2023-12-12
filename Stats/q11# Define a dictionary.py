#11)
# Define a dictionary
student_info = {
    'name': 'John Doe',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Physics', 'English']
}

# Access and print values from the dictionary
print("Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])
print("Courses:", ", ".join(student_info['courses']))

# Update a value in the dictionary
student_info['age'] = 21

# Add a new key-value pair to the dictionary
student_info['major'] = 'Computer Science'

# Access and print updated values
print("\nUpdated Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])
print("Courses:", ", ".join(student_info['courses']))
print("Major:", student_info['major'])


