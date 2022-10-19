# # Given two strings s and t, determine if they are isomorphic.

# # Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# # All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# s = "egf"
# t = "add"

# if len(s) != len(t):
#     print(False)
# hash_1 = {}
# hash_2 = {}
# arr = []
# for i, x in enumerate(s):
#     if x not in hash_1 and t[i] != hash_2:
#         hash_1[x] = t[i]
#         hash_2[t[i]] = x
#     elif (x in hash_1 or t[i] in hash_2) and (hash_1[x] != t[i] or hash_2[t[i]] != x):
#         print (False)
#     else: print(True)

# print(hash)

# # hash = {"i":"o"}
# # print(hash.get)





