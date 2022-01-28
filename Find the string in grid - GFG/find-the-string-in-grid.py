#User function Template for python3

class Solution:
	def searchWord(self, grid, word):
		# Code here
		def hs(i,j):
		    x=i
		    y=j
		    k=0
		    while(i<n and j<m and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i+=1
		        j+=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(i>=0 and j<m and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i-=1
		        j+=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(i<n and j>=0 and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i+=1
		        j-=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(i>=0 and j>=0 and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i-=1
		        j-=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(i<n and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i+=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(j<m and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        j+=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(i>=0 and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        i-=1
		    if(k==p):
		        return 1
		    i=x
		    j=y
		    k=0
		    while(j>=0 and k<p):
		        if(grid[i][j]!=word[k]):
		            break
		        k+=1
		        j-=1
		    if(k==p):
		        return 1
		    return 0
		n=len(grid)
		m=len(grid[0])
		p=len(word)
		ans=[]
		for i in range(n):
		    for j in range(m):
		        if(grid[i][j]==word[0]):
		            if(hs(i,j)):
		                ans.append([i,j])
		return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends