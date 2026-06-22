class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        for p in range(0, len(prices)):
            for q in range(p + 1, len(prices)):
                most = max(most, prices[q]-prices[p])
                print(q)

            
        return most