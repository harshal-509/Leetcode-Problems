class Solution:        
    def getMinRotations(self, A, B, num):
        minRotations = 0
        for i in range(len(A)):
            if A[i] != num and B[i] != num:
                return sys.maxsize
            minRotations += int(A[i] != num)
        return minRotations
    
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        minRotations = sys.maxsize
        for num in [tops[0], bottoms[0]]:
            minRotations = min(minRotations, self.getMinRotations(tops, bottoms, num), self.getMinRotations(bottoms, tops, num))
        return -1 if minRotations == sys.maxsize else minRotations