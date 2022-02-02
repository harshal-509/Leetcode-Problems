#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, m):
        # code here
        arr.sort()
        ans=set()
        n=len(arr)
        for i in range(n-3):
            for j in range(i+1,n-2):
                k=j+1
                l=n-1
                while(k<l):
                    t=arr[i]+arr[j]+arr[k]+arr[l]
                    if(t==m):
                        ans.add((arr[i],arr[j],arr[k],arr[l]))
                        l-=1
                    elif(t<m):
                        k+=1
                    else:
                        l-=1
        return sorted(ans)
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