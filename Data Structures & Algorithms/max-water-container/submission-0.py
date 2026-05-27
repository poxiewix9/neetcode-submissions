class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_sum = 0

        while left < right:
            current_area = min(heights[left], heights[right]) * (right - left)
            
            if current_area > max_sum:
                max_sum = current_area
            
            if heights[left] < heights[right]:
                left += 1 
            else:
                right -= 1 

        return max_sum