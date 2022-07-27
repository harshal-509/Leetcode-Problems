class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def check(temp):
            t=0
            for i in range(n):
                if(temp[i]==needs[i]):
                    t+=1
                if(temp[i]>needs[i]):
                    return 0
            if(t==n):
                return 1
            return -1
        def solve(temp):
            x=check(temp)
            if(x==1):
                return 0
            if(x==0):
                return float('inf')
            s=0
            for i in range(n):
                temp1[i]=temp[i]
                if(temp[i]<needs[i]):
                    s+=(needs[i]-temp[i])*price[i]
                    temp[i]=needs[i]
            ans=solve(temp)+s
            for i in range(n):
                temp[i]=temp1[i]
            for i in special:
                for j in range(n):
                    temp[j]+=i[j]
                ans=min(ans,solve(temp)+i[-1])
                for j in range(n):
                    temp[j]-=i[j]
            return ans
        n=len(price)
        temp=[0 for i in range(n)]
        temp1=[0 for i in range(n)]
        return solve(temp)