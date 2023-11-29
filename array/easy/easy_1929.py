# 1929. Concatenation of Array
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]


def getConcatenation(nums=[4, 8, 5, 8]):
    resp = nums.copy()
    resp.extend(nums)
    return resp


nums = [1, 2, 1]
print(f"inputs -> {nums}\noutputs -> {getConcatenation(nums=nums)}")
#
# inputs -> [1, 2, 1]
# outputs -> [1, 2, 1, 1, 2, 1]
