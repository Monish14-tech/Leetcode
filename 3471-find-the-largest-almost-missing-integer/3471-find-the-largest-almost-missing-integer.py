class Solution:
    def largestInteger(self, nums, k):
        count = {}

        for i in range(len(nums) - k + 1):
            subarray = set(nums[i:i + k])

            for num in subarray:
                count[num] = count.get(num, 0) + 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans