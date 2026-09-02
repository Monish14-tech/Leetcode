class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # We have selected k numbers
            if len(path) == k:
                result.append(path[:])
                return

            # Try every possible number
            for i in range(start, n + 1):
                path.append(i)

                backtrack(i + 1, path)

                path.pop()

        backtrack(1, [])

        return result