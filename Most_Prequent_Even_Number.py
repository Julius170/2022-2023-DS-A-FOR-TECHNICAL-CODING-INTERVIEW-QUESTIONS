# from collections import Counter

# # TEST CASE 1
# nums = [0,1,2,2,4,4,1]
# # Output = 2

# # TEST CASE 2 
# # nums = [4,4,4,9,2,4]
# # Output: 4

# # TEST CASE 3
# nums = [29,47,21,41,13,37,25,7]
# # Output = -1

# # TEST CASE 4
# nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
# # Output = 3346


# ans = ""
# even = [i for i in nums if i%2 == 0]
# high = [0]

# even = Counter(even).most_common()

# print(even)

# if even== []:
#     print(-1)
# elif even[0][1] == even[1][1]:
#     print(min(even[0][0], even[1][0]))
#     print(even[0][1], even[1][0])
# else:
#     print(even[0][0])

# print(even[0][1], even[1][0])


# num1 = 2

# num2 = 3

# ans = 0
# while num1 > 0 and num2 > 0:
#     if num1 < num2:
#         num2 -=  num1
#         ans += 1 
#     else:
#         num1 -= num2
#         ans += 1
# print(ans)
