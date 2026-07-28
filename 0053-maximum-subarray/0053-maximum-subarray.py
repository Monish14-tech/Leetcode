class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        ans=nums[0]
        for i in nums:
            current+=i
            ans=max(ans,current)
            if current<0:
                current=0
        return ans
