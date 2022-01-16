class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n=len(seats)
        x=seats.count(1)
        if(x==1):
            m=seats.index(1)
            return max(m,n-m-1)
        else:
            a=-1
            b=-1
            ans=-1
            for i in range(n):
                if(a==-1 and seats[i]==1):
                    a=i
                elif(b==-1 and seats[i]==1):
                    b=i
                elif(seats[i]==1):
                    a=b
                    b=i
                if(a!=-1 and b!=-1):
                    ans=max(ans,(b-a)//2)
                if(a!=-1 and b==-1):
                    ans=max(ans,a)
            ans=max(ans,n-b-1)
            return ans
                    