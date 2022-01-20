#User function Template for python3
class Solution:
    def rearrange(self,arr, m):
        # code here
        pos=[]
        neg=[]
        n,p=0,0
        for i in range(m):
            if(arr[i]<0):
                neg.append(arr[i])
                n+=1
            else:
                pos.append(arr[i])
                p+=1
        q=0
        i=0
        j=0
        k=0
        while(i<m and j<p and k<n):
            if(q%2==0):
                arr[i]=pos[j]
                j+=1
            else:
                arr[i]=neg[k]
                k+=1
            q+=1
            i+=1
        while(i<m and j<p):
            arr[i]=pos[j]
            j+=1
            i+=1
        while(i<m and k<n):
            arr[i]=neg[k]
            k+=1
            i+=1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends