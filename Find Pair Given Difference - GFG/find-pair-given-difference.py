#User function Template for python3
class Solution:
    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        i=0
        j=L-1
        for i in range(L):
            x=arr[i]+N
            y=arr[i]-N
            j=0
            k=L-1
            while(j<=k):
                m=j+(k-j)//2
                if(arr[m]==x):
                    return 1
                if(arr[m]<x):
                    j=m+1
                else:
                    k=m-1
            j=0
            k=L-1
            while(j<=k):
                m=j+(k-j)//2
                if(arr[m]==y):
                    return 1
                if(arr[m]<y):
                    j=m+1
                else:
                    k=m-1
        return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends