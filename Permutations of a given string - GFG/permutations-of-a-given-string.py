#User function Template for python3

class Solution:
    def find_permutation(self, s):
        # Code here
        def solve(i):
            if(i==n):
                ans.append("".join(s))
            for j in range(i,n):
                s[i],s[j]=s[j],s[i]
                solve(i+1)
                s[i],s[j]=s[j],s[i]
        ans=[]
        temp=""
        s=list(s)
        n=len(s)
        solve(0)
        return sorted(ans)
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends