
#Q9)program for postfix evaluation
def postfix_evaluation(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:   
            if len(stack) >= 2:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if char == "+":
                    stack.append(operand1 + operand2)
                elif char == "-":
                    stack.append(operand1 - operand2)
                elif char == "*":
                    stack.append(operand1 * operand2)
                elif char == "/":
                    stack.append(float(operand1) / operand2)
                elif char == "^":
                    stack.append(operand1 ** operand2)
            else:
                return "Invalid expression"
    if len(stack) == 1:
        return stack.pop()
    else:
        return "Invalid expression"
expression = input("Enter the postfix expression: ")
result = postfix_evaluation(expression)
print("Result:", result)