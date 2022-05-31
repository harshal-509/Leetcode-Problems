class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
        Intervals.sort()
        ans=[Intervals[0]]
        i=1
        while(i<n):
            if(ans[-1][1]>=Intervals[i][0]):
                ans[-1][0]=min(ans[-1][0],Intervals[i][0])
                ans[-1][1]=max(ans[-1][1],Intervals[i][1])
            else:
                ans.append(Intervals[i])
            i+=1
        return ans
#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends