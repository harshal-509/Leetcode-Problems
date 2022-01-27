#User function Template for python3

class Solution:
    def nextPermutation(self, n, arr):
        # code here
        ans=-11
        for i in range(n-2,-1,-1):
            if(arr[i]<arr[i+1]):
                ans=i
                break
        if(ans==-11):
            arr.sort()
            return arr
        ans1=i+1
        for i in range(ans+1,n):
            if(arr[i]>=arr[ans] and arr[i]<arr[ans1]):
                ans1=i
        arr[ans],arr[ans1]=arr[ans1],arr[ans]
        arr=arr[:ans+1]+arr[n:ans:-1]
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends