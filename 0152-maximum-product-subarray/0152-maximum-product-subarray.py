class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]

        for i in range(n):
            product = 1

            for j in range(i, n):
                product *= nums[j]
                ans = max(ans, product)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            ans = max(ans, curr_max)

        return ans
        return ans