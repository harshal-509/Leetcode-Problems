#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        i=0
        s2=s2+s2
        n=len(s2)
        m=len(s1)
        if(m!=n//2):
            return 0
        while(i<n):
            if(s1[0]==s2[i]):
                j=i
                k=0
                while(k<m and j<n):
                    if(s1[k]!=s2[j]):
                        break
                    j+=1
                    k+=1
                if(k==m):
                    return 1
                else:
                    i=j
            else:
                i+=1
        return 0
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
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends