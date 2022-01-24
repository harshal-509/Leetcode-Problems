#User function Template for python3

from bisect import bisect_right as upper_bound
class Solution:
    def median(self, matrix, r, c):
    	#code here
    	def binaryMedian(m, r, d):
            mi = m[0][0]
            mx = 0
            for i in range(r):
                if m[i][0] < mi:
                    mi = m[i][0]
                if m[i][d-1] > mx :
                    mx =  m[i][d-1]
             
            desired = (r * d + 1) // 2
             
            while (mi < mx):
                mid = mi + (mx - mi) // 2
                place = [0];
                 
                # Find count of elements smaller than mid
                for i in range(r):
                     j = upper_bound(m[i], mid)
                     place[0] = place[0] + j
                if place[0] < desired:
                    mi = mid + 1
                else:
                    mx = mid
            return mi  
        return binaryMedian(matrix,r,c)
    	  
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends