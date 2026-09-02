class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):

                # Starting cell
                if i == 0 and j == 0:
                    continue

                # First row
                if i == 0:
                    grid[i][j] += grid[i][j - 1]

                # First column
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]

                # Other cells
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[rows - 1][cols - 1]