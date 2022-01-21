
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        a=[0 for i in range(n)]
        b=[0 for i in range(n)]
        t=0
        s=0
        for i in range(n):
           t=max(t,arr[i])
           s=max(s,arr[n-i-1])
           a[i]=t
           b[n-i-1]=s
        ans=0
        for i in range(n):
            ans+=min(a[i],b[i])-arr[i]
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends