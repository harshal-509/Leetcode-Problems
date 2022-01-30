#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        h={}
        n=len(str1)
        m=len(str2)
        if(n!=m):
            return 0
        for i in range(n):
            if(str1[i] in h):
                if(h[str1[i]]!=str2[i]):
                    return 0
            else:
                h[str1[i]]=str2[i]
        h={}
        for i in range(n):
            if(str2[i] in h):
                if(h[str2[i]]!=str1[i]):
                    return 0
            else:
                h[str2[i]]=str1[i]
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends