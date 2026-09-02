class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            # All numbers are selected
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Already used
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack(path, used)

                # Undo
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result