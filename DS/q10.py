# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:05:41 2023

@author: Pratham
"""

#Q10)program for matching parenthesis
def check_matching_parentheses(input_string):
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    stack = []
    for char in input_string:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack:
                return False
            current_opening = stack.pop()
            if opening_parentheses.index(current_opening) != closing_parentheses.index(char):
                return False
        return len(stack) == 0
input_str = input("Enter a string with parentheses: ")
if check_matching_parentheses(input_str):
    print("Parentheses are matching.")
else:
    print("Parentheses are not matching.")