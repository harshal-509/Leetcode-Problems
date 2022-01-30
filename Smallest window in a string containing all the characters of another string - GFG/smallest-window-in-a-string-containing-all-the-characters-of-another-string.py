#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, t):
        #code here
        c=len(set(t))
        h=[0 for i in range(256)]
        p=[0 for i in range(256)]
        for i in t:
            h[ord(i)]+=1
        i,j,q=0,0,0
        n=len(s)
        ans=[0,n+2]
        while(i<n):
            if(p[ord(s[i])]==h[ord(s[i])]-1):
                q+=1
            p[ord(s[i])]+=1
            if(c==q):
                while(p[ord(s[j])]>h[ord(s[j])] and j<i):
                    p[ord(s[j])]-=1
                    j+=1
                if(i-j+1<ans[1]-ans[0]):
                    ans[0]=j
                    ans[1]=i+1
            i+=1
        if(ans[0]==0 and ans[1]==n+2):
            return -1
        return s[ans[0]:ans[1]]
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
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends