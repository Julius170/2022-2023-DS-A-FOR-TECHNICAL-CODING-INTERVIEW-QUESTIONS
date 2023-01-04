# Input: 

# TEST 1
# nums = [1,2,3,4]
# Output: [1,3,6,10]

nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

for i in range (1, len(nums)):
    nums[i] += nums[i-1]
print(nums)