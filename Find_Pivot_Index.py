# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.


nums = [1,7,3,6,5,6]

total = sum(nums)
l = 0

for i in range(len(nums)):
    r = total - l - nums[i]
    if r == l:
        print(i)
    l+= nums[i]
print(0)

