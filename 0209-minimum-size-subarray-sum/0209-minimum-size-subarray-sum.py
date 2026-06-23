class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0
        total = 0
        min_len = float("inf")

        for right in range(len(nums)):

            total += nums[right]

            while total >= target:

                min_len = min(
                    min_len,
                    right - left + 1
                )

                total -= nums[left]
                left += 1

        if min_len == float("inf"):
            return 0

        return min_len