#User function Template for python3

class Solution:
    def find_permutation(self, s):
        # Code here
        n=len(s)
        def hs(s,i,ans):
            if(i==n):
                ans.append("".join(s))
            for j in range(i,n):
                s[i],s[j]=s[j],s[i]
                hs(s,i+1,ans)
                s[i],s[j]=s[j],s[i]
        ans=[]
        s=list(s)
        hs(s,0,ans)
        ans.sort()
        return ans
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