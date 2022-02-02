#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, m):
        # code here
           li = set()
           n = len(arr)
           arr.sort()
           for i in range(n-3):
               for j in range(i+1, n-2):
                   l = j + 1
                   r = n - 1
                   while(l < r):
                       s = arr[i] + arr[j] + arr[l] + arr[r]
                       if (s == k):
                           li.add((arr[i], arr[j], arr[l], arr[r]))
                           l += 1
                           r -= 1
                       elif (s < k):
                           l += 1
                       else :
                           r -= 1
           return sorted(li) 
#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends