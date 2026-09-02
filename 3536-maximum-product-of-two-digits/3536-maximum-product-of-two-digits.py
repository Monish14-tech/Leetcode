class Solution:
    def maxProduct(self, n):
        digits = []

        while n > 0:
            digit = n % 10
            digits.append(digit)
            n //= 10

        digits.sort()

        return digits[-1] * digits[-2]