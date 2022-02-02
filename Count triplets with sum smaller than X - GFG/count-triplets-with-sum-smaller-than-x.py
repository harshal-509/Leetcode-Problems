class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort()
        ans=0
        for i in range(n):
            j=i+1
            k=n-1
            while(j<k):
                t=arr[i]+arr[j]+arr[k]
                if(t>=sumo):
                    k-=1
                else:
                    ans+=k-j
                    j+=1
        return ans
                
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends