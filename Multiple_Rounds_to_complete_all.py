""" 
You are given a 0-indexed integer array tasks, 
where tasks[i] represents the difficulty level of a task. In each round, 
you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 
if it is not possible to complete all the tasks. 

"""
from collections import Counter
import math

def minimumRounds(tasks=[2,2,3,3,2,4,4,4,4,4]):
    d = Counter(tasks)
    res = 0
    for i in d:
        n = d[i]
        if n <= 1:
            return(-1)
        else: 
            res += math.ceil(n/3)
            return(res)



    
minimumRounds()


