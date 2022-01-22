class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy=-100001
        first_sell=0
        second_buy=-100001
        second_sell=0
        n=len(prices)
        for i in range(n):
            first_buy=max(first_buy,-prices[i])
            first_sell=max(first_sell,first_buy+prices[i])
            second_buy=max(second_buy,first_sell-prices[i])
            second_sell=max(second_sell,second_buy+prices[i])
        return second_sell