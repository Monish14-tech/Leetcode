class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)

        dp = nums[:]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                take_left = nums[left] - dp[left + 1]
                take_right = nums[right] - dp[left]

                dp[left] = max(take_left, take_right)

        return dp[0] >= 0