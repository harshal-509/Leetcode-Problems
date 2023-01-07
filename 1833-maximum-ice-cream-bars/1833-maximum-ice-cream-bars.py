class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        a=0
        s=0
        for i in costs:
            if(s+i<=coins):
                a+=1
                s+=i
            else:
                return a
        return a