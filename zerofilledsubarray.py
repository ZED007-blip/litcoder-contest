import sys
def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# User input for the list of numbers
nums_input = input("Enter the list of numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))

# Calculate and print the result
result = max_subarray_sum(nums)
print("Output:", result)
