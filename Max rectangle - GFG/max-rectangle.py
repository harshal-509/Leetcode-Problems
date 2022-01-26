#User function Template for python3
class Solution:
    def maxArea(self,mat, n, m):
        # code here
        left=[0 for i in range(m)]
        right=[0 for i in range(m)]
        def maxareahistogram(arr,n):
            s=[]
            for i in range(n):
                if(s):
                    while(s and arr[s[-1]]>=arr[i]):
                        s.pop()
                    if(s):
                        left[i]=s[-1]+1
                        s.append(i)
                    else:
                        left[i]=0
                        s.append(i)
                else:
                    s.append(0)
                    left[i]=0
            s=[]
            for i in range(n-1,-1,-1):
                if(s):
                    while(s and arr[s[-1]]>=arr[i]):
                        s.pop()
                    if(s):
                        right[i]=s[-1]-1
                        s.append(i)
                    else:
                        right[i]=n-1
                        s.append(i)
                else:
                    s.append(i)
                    right[i]=i
            ans=0
            for i in range(n):
                ans=max(ans,(right[i]-left[i]+1)*arr[i])
            return ans
        ans=maxareahistogram(mat[0],m)
        for i in range(1,n):
            for j in range(m):
                if(mat[i][j]):
                    mat[i][j]+=mat[i-1][j]
            ans=max(ans,maxareahistogram(mat[i],m))
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends