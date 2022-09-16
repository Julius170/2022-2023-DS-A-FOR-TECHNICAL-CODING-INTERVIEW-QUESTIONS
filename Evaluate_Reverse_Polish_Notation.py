
# Test Case 
# tokens = ["2","1","+","3","*"]  # answer = 9

# tokens = ["4","13","5","/","+"] #answer =  6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # answer 22


# Solution 
# Using a stack:

stack = []
# Loping through every charaters in the token array:
for i in tokens:

# If the character is an operator: remove the last 2 characters as operands and use the operatior on the operands,
# and append the resultto the stack
    if i == "+" :
        x = int(stack.pop())
        y = int(stack.pop())
        print(int(x+y))
        stack.append(x + y)
    elif i == "*":
        x = int(stack.pop())
        y = int(stack.pop())
        print(int(x*y))
        stack.append(int(x * y))
    elif i == "-":
        x = int(stack.pop())
        y = int(stack.pop())
        print(int(y-x))
        stack.append(y - x)
    elif i == "/":
        x = int(stack.pop())
        y = int(stack.pop())
        print(int(y/x))
        stack.append(int(y / x))
# Otherwise add the current chracter to the stack
    elif i.isnumeric() or type(int(i) == int):
        stack.append(i)

