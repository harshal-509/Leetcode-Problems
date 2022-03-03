#User function Template for python3
import heapq
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __lt__(self, nxt):
        return self.data < nxt.data
class Solution:
    def huffmanCodes(self,s,f,n):
        # Code here
        def preorder(root,temp):
            if(root==None):
                return
            if(root.left==None and root.right==None):
                ans.append("".join(temp.copy()))
                return
            temp.append('0')
            preorder(root.left,temp)
            temp.pop()
            temp.append('1')
            preorder(root.right,temp)
            temp.pop()
        s=[]
        heapq.heapify(s)
        for i in f:
            s.append(Node(i))
        heapq.heapify(s)
        while(len(s)>1):
            x=heapq.heappop(s)
            y=heapq.heappop(s)
            root=Node(x.data+y.data)
            root.left=x
            root.right=y
            heapq.heappush(s,root)
        root=heapq.heappop(s)
        temp=[]
        ans=[]
        preorder(root,temp)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S= input()
		N= len(S);
		f= [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.huffmanCodes(S,f,N)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends