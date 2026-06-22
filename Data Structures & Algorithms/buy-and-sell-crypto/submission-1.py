class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_left = float('inf')
        ans = 0

        for p in prices:
            if p < least_left:
                least_left = p
            else:
                ans = max(ans, p - least_left)

        return ans