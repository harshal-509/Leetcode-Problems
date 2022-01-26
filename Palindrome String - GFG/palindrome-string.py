#User function Template for python3
class Solution:
	def isPalindrome(self, s):
		# code here
		i=0
		j=len(s)-1
		while(i<j):
		    if(s[i]!=s[j]):
		        return 0
		    i+=1
		    j-=1
		return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends