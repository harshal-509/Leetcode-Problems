#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        if(arr[0]==0):
            return 1
        for i in range(1,n):
            if(arr[i]==0):
                return 1
            arr[i]=arr[i]+arr[i-1]
        h=Counter(arr)
        if(h[0]):
            return 1
        for i in h:
            if(h[i]>=2):
                return 1
        return 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends