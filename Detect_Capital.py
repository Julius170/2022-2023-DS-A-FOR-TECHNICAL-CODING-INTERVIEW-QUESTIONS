# Input:
# TEST 1 
# word = "USA"
# Output: true

# TEST 2
word = "FlaG"
# Output: fasle

# ans_arr = ""
# arr = ""
# for i in word:
#     if i.islower():
#         ans_arr += "0"
#     elif i.isupper():
#         ans_arr+= "1"

# print(ans_arr)

# if ans_arr == "0"*len(word):
#     print(True)
# elif ans_arr == "1"*len(word):
#     print(True)
# elif ans_arr == ("1"+("0"*(len(word)-1))):
#     print(True)
# else: print(False)

# OR

if word.islower() == True or word.isupper() == True:
    print(True)
elif word[0].isupper() == True and word[1:len(word)].islower() == True:
    print(True)
else: 
    print(False)

