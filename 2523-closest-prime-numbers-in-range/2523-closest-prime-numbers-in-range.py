class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def fillPrimes(chprime, high):
            ck = [True]*(high+1)
            l = int(math.sqrt(high))
            for i in range(2, l+1):
                if ck[i]:
                    for j in range(i*i, l+1, i):
                        ck[j] = False
            for k in range(2, l+1):
                if ck[k]:
                    chprime.append(k)
        def segmentedSieve(low, high):
            chprime = list()
            fillPrimes(chprime, high)
            prime = [True] * (high-low + 1)
            for i in chprime:
                lower = (low//i)
                if lower <= 1:
                    lower = i+i
                elif (low % i) != 0:
                    lower = (lower * i) + i
                else:
                    lower = lower*i
                for j in range(lower, high+1, i):
                    prime[j-low] = False
            ans=[]
            for k in range(max(2,low), high + 1):
                    if prime[k-low]:
                        ans.append(k)
            return ans
        p=segmentedSieve(left,right)
        if(len(p)<=1):
            return [-1,-1]
        mindis=float('inf')
        ans=[-1,-1]
        for i in range(len(p)-1):
            x=p[i]
            y=p[i+1]
            if(y-x<mindis):
                mindis=y-x
                ans[0]=x
                ans[1]=y
        return ans