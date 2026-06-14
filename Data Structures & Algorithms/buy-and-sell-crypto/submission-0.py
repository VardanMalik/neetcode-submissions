class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        hightestProfit = 0
        for r in range(len(prices)):
            if prices[r]> prices[l]:
                profit = prices[r]- prices[l]
                hightestProfit = max(hightestProfit, profit)
            else:
                l = r
            r+=1
        return hightestProfit