class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        n=len(matches)
        h=[[0,0] for i in range(100001)]
        t=Counter([])
        for i in range(n):
            h[matches[i][0]][0]+=1
            h[matches[i][1]][1]+=1
        l=[]
        r=[]
        for i in range(100001):
            if(h[i][1]==1):
                l.append(i)
            elif(h[i][0] and h[i][1]==0):
                r.append(i)
        return [r,l]