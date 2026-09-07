class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        left_most = [-1] * n

        for i in range(n-1,-1,-1):
            while stack and heights[i] < heights[stack[-1]]:
                left_most[stack.pop()] = i
            stack.append(i)

        stack = []
        right_most = [n] * n

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                right_most[stack.pop()] = i
            stack.append(i)

        max_area = max(heights)

        for i in range(n):
            curr_area = (right_most[i] - left_most[i] -1) * heights[i] 
            max_area = max(max_area, curr_area)

        return max_area