class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        z=Counter([])
        ans=0
        for i in nums:
            n=i
            while n % 2 == 0:
                if(z[2]==0):
                    ans+=1
                    z[2]=1
                n = n / 2
            for i in range(3,int(math.sqrt(n))+1,2):
                while n % i== 0:
                    if(z[i]==0):
                        ans+=1
                        z[i]=1
                    n = n / i
            if n > 2:
                if(z[n]==0):
                    z[n]+=1
                    ans+=1
        return ans