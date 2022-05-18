#User function Template for python3
import heapq
class Solution:
    def solve(self, arr, n):
        # code here
        heapq.heapify(arr)
        a="0"
        b="0"
        while(arr):
            a+=str(heapq.heappop(arr))
            if(arr):
                b+=str(heapq.heappop(arr))
        return int(a)+int(b)
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends