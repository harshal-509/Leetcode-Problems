class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[]
        n=len(potions)
        potions.sort()
        for i in spells:
            t=int(math.ceil(success/i))
            ans.append(n-bisect.bisect_left(potions,t))
        return ans