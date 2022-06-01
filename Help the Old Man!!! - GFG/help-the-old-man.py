#User function Template for python3

class Solution:
    def __init__(self):
        self.ans=0
        self.y=0
    def shiftPile(self, N, k):
        # code here
        def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
            if n == 0:
                return [0,0]
            TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
            self.ans+=1
            if(self.ans==k):
                self.y=[from_rod,to_rod]
            TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
        TowerOfHanoi(N,'1','3','2')
        return self.y
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, n = [int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.shiftPile(N, n)
        print(ans[0]+" "+ans[1])
# } Driver Code Ends