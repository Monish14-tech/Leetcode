class Solution:
    def arrayRankTransform(self, arr):
        sorted_arr = sorted(set(arr))

        rank = {}

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1

        result = []

        for num in arr:
            result.append(rank[num])

        return result