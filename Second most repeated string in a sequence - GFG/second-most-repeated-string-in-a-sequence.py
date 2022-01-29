#User function Template for python3
from collections import Counter
class Solution:
    def secFrequent(self, arr, n):
        # code here
        return Counter(arr).most_common(2)[-1][0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends