class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_day=float('inf')
        second_day=-1
        prices_length=len(prices)
        solution=0
        for i in range(prices_length):
            if(prices[i]<first_day):
                first_day=prices[i]
                second_day=prices[i]
            second_day=prices[i]
            if(second_day-first_day>0):
                solution+=second_day-first_day
                first_day=prices[i]
                second_day=prices[i]
        return solution