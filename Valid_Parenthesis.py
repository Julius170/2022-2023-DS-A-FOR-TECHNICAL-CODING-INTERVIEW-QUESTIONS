# LeetCode: Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Test Cases 
# s = "()[]{}" # True
# s = "(]"     # False
s = "(){}}{"   # False

# Function Solution 
def ValidParenthesis(s):
    stack = []
    top = 0
    for i in s:
# Getting the bracket at the top of the stack
        if len(stack) ==1:
            top = stack[0]
        elif len(stack) > 1:
            top = stack[-1]
        else: top = 0
# If it is an opening bracket, add it to the stack
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
# If it is a closing bracket, check if the top of the stack is the corresponding opening bracket
# If it is? pop the top of the stack
        elif i == ")" and top == "(":
            print("()")
            stack.pop() 
        elif i == "]" and top == "[":
            stack.pop()
            print("[]")
        elif i == "}" and top == "{":
            stack.pop()  
            print("{}")
#  Else return False (in any other cases)
        else:
            return False
# If there are are no other bracket left in the stack, return True
# else return False
    if len(stack) ==0:
        return True
    else: return False
            




print(ValidParenthesis(s))

