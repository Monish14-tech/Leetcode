class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        heights.append(0)

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area