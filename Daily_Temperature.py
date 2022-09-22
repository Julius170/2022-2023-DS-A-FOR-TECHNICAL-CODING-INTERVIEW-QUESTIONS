from tkinter.messagebox import QUESTION


# QUESTION 

# Given an array of integers temperatures represents the daily temperatures,
#  return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# TEST CASES
temperatures = [73,74,75,71,69,72,76,73]


# SOLUTION
stack = []
count = 0
res = []

for i, x in enumerate(temperatures):
    print(i, x)
    while i <= len(temperatures):
        i+=1
        if temperatures[i] <= x:
            count +=1
        elif temperatures[i] >= x:
            count+=1
            res.append(count)
            count = 0
        i+=1

print(res)