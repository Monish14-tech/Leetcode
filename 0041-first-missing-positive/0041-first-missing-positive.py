class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        i=1
        while True:
            if i not in s:
                return i
            i+=1
       