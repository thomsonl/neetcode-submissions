class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # lowest height * distance
        left = 0
        ans = 0

        while left < len(heights) / 2 + 1:
            right = len(heights) - 1
            while right > left:
                ans = max(ans, min(heights[left], heights[right]) * (right - left))
                right -= 1
            left += 1
        
        return ans