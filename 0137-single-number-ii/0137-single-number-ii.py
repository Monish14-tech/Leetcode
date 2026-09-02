class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        is_neg = 0
        for i in range(32):
            summ = 0
            for num in nums:
                if num < 0:
                    is_neg = is_neg+1
                last_bit = (abs(num) >> i) & 1
                summ = summ+last_bit
            summ = summ%3
            if summ != 0:
                summ = summ <<i
                ans = ans | summ
        if is_neg%3 !=0:
            return -ans
        return ans


        