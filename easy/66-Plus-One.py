class Solution:
    def plusOne(self, digits):
        number = int("".join(map(lambda x: str(x), digits))) + 1
        return [int(item) for item in list(str(number))]


print(Solution().plusOne(digits=[4, 3, 2, 1]))
