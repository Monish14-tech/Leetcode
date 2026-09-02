class Solution:
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)

        while b != 0:
            a, b = b, a % b

        return a