#User function Template for python3
class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n=len(s)
	    def hs(s,i,temp,ans):
	        if(i==n):
	            if(len(temp)!=0):
	                ans.append("".join(temp.copy()))
	            return
	        hs(s,i+1,temp,ans)
	        temp.append(s[i])
	        hs(s,i+1,temp,ans)
	        temp.pop()
	    temp=[]
	    ans=[]
	    hs(s,0,temp,ans)
	    ans.sort()
	    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends