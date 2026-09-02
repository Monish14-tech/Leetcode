class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        # Convert 2D to 1D
        arr = []

        for row in grid:
            for num in row:
                arr.append(num)

        # Shift
        k = k % (m * n)
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D
        result = []

        for i in range(0, len(arr), n):
            result.append(arr[i:i + n])

        return result