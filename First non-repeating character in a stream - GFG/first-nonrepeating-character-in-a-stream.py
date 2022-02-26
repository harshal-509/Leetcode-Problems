
class Solution:
	def FirstNonRepeating(self, s):
		# Code here
		h=[[0,-1] for i in range(26)]
		ans=""
		n=len(s)
		for i in range(n):
		    h[ord(s[i])-97][0]+=1
		    h[ord(s[i])-97][1]=i
		    flag=0
		    t=0
		    k=100001
		    for i in range(26):
		        if(h[i][0]==1):
		            flag=1
		            if(k>h[i][1]):
		                t=i
		                k=h[i][1]
	        if(flag):
	            ans+=chr(t+97)
	        else:
	            ans+="#"
	    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends