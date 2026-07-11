class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        ans = []
        i = 0

        for x in range(1, len(nums) + 1):
            while i < len(nums) and nums[i] < x:
                i += 1

            if i == len(nums) or nums[i] != x:
                ans.append(x)

        return ans