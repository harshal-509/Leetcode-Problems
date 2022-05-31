#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        s=[i for i in range(n)]
        while(len(s)>=2):
            x=s.pop()
            y=s.pop()
            if(M[x][y]==1 and M[y][x]==0):
                s.append(y)
            elif(M[x][y]==0 and M[y][x]==1):
                s.append(x)
        if()
        t=s[0]
        for i in range(n):
            if((t==i) or M[t][i]==0 and M[i][t]==1):
                pass
            else:
                return -1
        return t
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends