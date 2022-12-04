class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans=0
        n=len(skill)
        i=0
        j=n-1
        x=-1
        while(i<j):
            if(x==-1 or x==skill[i]+skill[j]):
                x=skill[i]+skill[j]
                ans+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return ans