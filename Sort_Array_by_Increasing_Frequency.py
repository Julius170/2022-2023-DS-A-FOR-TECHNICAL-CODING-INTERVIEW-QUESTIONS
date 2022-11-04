# EASY =>> Arrays, Strings
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.

# TEST CASE 1
from collections import Counter


# nums = [1,1,2,2,2,3,3]
# Output: [3,1,1,2,2,2]


# TEST CASE 2
nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]

ans = []
res = []
d = Counter(nums)
d = (d.most_common())

d.sort(key = lambda x: x[0], reverse=True)
d.sort(key = lambda x: x[1])

print(d)

for i in d:
    ans.append([*str(i[0])*(i[1])])

print(ans)

t = []
for i in d:
    a, b = i
    t.extend([a]*b)
print(t)