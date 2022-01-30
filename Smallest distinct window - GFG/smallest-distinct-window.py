#User function Template for python3
class Solution:
    def findSubString(self, s):
        # Your code goes here
        c=len(set(s))
        p=[0 for i in range(256)]
        i,j,q=0,0,0
        n=len(s)
        ans=n
        while(i<n):
            if(p[ord(s[i])]==0):
                q+=1
            p[ord(s[i])]+=1
            if(c==q):
                while(p[ord(s[j])]>1 and j<i):
                    p[ord(s[j])]-=1
                    j+=1
                ans=min(ans,i-j+1)
            i+=1
        ans=min(ans,i-j)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends