class Solution:
    def missingMultiple(self, nums, k):
        num = k

        while num in nums:
            num += k

        return num