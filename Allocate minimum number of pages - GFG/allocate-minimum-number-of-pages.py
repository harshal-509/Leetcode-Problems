class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,a, N, M):
        #code here
        def hs(m):
            t=1
            s=0
            for i in range(N):
                if(s+a[i]<=m):
                    s+=a[i]
                else:
                    t+=1
                    s=a[i]
                if(t>M or a[i]>m):
                    return 0
            return 1
                
        i=min(a)
        j=sum(a)
        ans=-1
        while(i<=j):
            m=i+(j-i)//2
            if(hs(m)):
                ans=m
                j=m-1
            else:
                i=m+1
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends