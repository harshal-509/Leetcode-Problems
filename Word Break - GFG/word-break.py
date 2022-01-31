#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    n=len(line)
    def hs(line,i):
        if(i==n):
            return 1
        ans=""
        ans1=0
        for j in range(i,n):
            ans+=line[j]
            if(ans in dictionary):
                ans1=ans1|hs(line,j+1)
        return ans1
    return hs(line,0)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends