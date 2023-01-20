# <1221> Split a String in Balanced Strings (EASY)

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
#     Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
def balancedStringSplit(s: str) -> int:
    res, flag = 0, 0
    for i in s:
        if i == "L":
            flag += 1
        else:
            flag -= 1
        
        if flag == 0:
            res+=1

    return res


print(balancedStringSplit("RLRRLLRLRL"))
# 4
