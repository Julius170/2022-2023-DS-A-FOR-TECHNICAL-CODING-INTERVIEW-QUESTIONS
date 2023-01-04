# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between 
# a letter in pattern and a non-empty word in s.

# Input
# TEST 1 
pattern = "abba"
s = "dog cat cat dog"

# TEST 2
# pattern = "abba"
# s = "dog cat cat fish"

# TEST 3
# pattern = "aaaa"
# s = "dog cat cat dog"


# TEST 4
pattern = "abba"
s = "dog dog dog dog"

# SOLUTION 

string = (s.split(" "))
print(string)
hash = {}
arr = []
if len(pattern) != len(string):
    print(False)
for i in pattern:
    if i not in hash and string[pattern.index(i)] not in hash.values():
        hash[i] = string[pattern.index(i)]
print(hash)

for i in pattern:
    if i in hash.keys():
        arr.append(hash[i])
print(arr)
if arr == string:
    print(True)
else:
    print(False)