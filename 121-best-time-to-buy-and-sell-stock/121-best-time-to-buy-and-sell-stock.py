class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=-100000000
        sell=0
        for i in prices:
            buy=max(buy,-i)
            sell=max(sell,i+buy)
        return sell