# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


def shuffle(nums, n):
    # Initialize an empty list to store the shuffled elements
    resp = []

    # Loop through half the length of the nums list
    for i in range(0, len(nums) // 2):
        # Append the first element from the current iteration
        resp.append(nums[i])
        # Append the element n positions away from the current element
        resp.append(nums[n + i])

    # Return the shuffled list
    return resp


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(shuffle(nums=nums, n=n))
#
# [2, 3, 5, 4, 1, 7]
