from typing import List


class Solution:
    def kthLargest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        ans=[]
        for i in range(n):
            a=0
            for j in range(i,n):
                a+=arr[j]
                ans.append(a)
        ans.sort(reverse=True)
        return ans[k-1]
                


#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends