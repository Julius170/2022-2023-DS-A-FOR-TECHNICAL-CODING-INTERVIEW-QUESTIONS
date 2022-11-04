# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# TEST CASE 

from collections import Counter

# TEST CASE 1
s = "tree"
# Output: "eert"

# TEST CASE 2 
# s = "cccaaa"
# Output: "aaaccc"

# TEST CASE 2
# s = "Aabb"
# Output = "bbAa"


ans = [] 
hash = {}
res = ""
new = Counter(s)
new  = new.most_common()

for i, v in new:
    # ans.append(i * v)
    ans.extend([i]*v)

print(ans)
# for i in ans:
#     res += i
res = ''.join(ans)
print(res)


