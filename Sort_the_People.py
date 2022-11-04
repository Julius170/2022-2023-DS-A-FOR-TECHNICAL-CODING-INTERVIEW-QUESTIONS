# EASY =>> Arrays, Strings

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# TEST CASE 1:
# names = ["Mary","John","Emma"]
# heights = [180,165,170]


# TEST CASE 2:
names = ["Alice","Bob","Bob"]
heights = [155,185,150]

# SOLUTION:
ans = []
sorted_height = sorted(heights)[::-1]
print(sorted_height)

for i in (sorted_height):
    ans.append(names[heights.index(i)])
print(ans)
    
