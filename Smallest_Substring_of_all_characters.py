arr = ['x','y','z']
arr_2 = ""
for i in arr:
    arr_2 += i 
str = "xyyzyzyx"

right, left = 0, len(arr)

# print(right, left)

moving_str = str[right: left]

while left < len(str) and len(moving_str) > len(arr):
    if len(moving_str) < len(arr) and sorted(moving_str) !=  sorted(arr_2):
        print("Nooo")
        left +=1
    elif len(moving_str) > len(arr) and sorted(moving_str) != sorted(arr_2):
        print("Noooo")
    elif len(moving_str) == len(arr) and sorted(moving_str) == sorted(arr_2):
        print("Yess")
    left+=1



