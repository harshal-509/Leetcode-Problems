#User function Template for python3
from collections import Counter
class Solution:
    def countKdivPairs(self, A, n, K):
        #code here
        freq = [0] * K
      
        # Count occurrences of all remainders
        for i in range(n):
            freq[A[i] % K]+= 1
              
        # If both pairs are divisible by 'K'
        sum = freq[0] * (freq[0] - 1) / 2;
          
        # count for all i and (k-i)
        # freq pairs
        i = 1
        while(i <= K//2 and i != (K - i) ):
            sum += freq[i] * freq[K-i]
            i+= 1
      
        # If K is even
        if( K % 2 == 0 ):
            sum += (freq[K//2] * (freq[K//2]-1)/2);
          
        return int(sum)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = int(input())
        ob= Solution()
        print(ob.countKdivPairs(a,n,k))
# } Driver Code Ends