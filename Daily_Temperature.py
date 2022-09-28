# QUESTION 
# FACEBOOK => STACKS
# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# TEST CASES
temperatures = [73,74,75,71,69,72,76,73]    #[1,1,4,2,1,1,0,0]



# SOLUTION
stack = []
ans = []
    
for i, t in enumerate(temperatures):
    while stack and stack[-1][0] < t:
        val, index = stack.pop()
        ans[index] = i - index
    
    stack.append((t, i))
    ans.append(0)
print(ans)
