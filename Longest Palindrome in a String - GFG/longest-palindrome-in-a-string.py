#User function Template for python3

class Solution:
    def longestPalin(self, s):
        # code here
        n=len(s)
        ans=[0,0]
        for i in range(n):
            j=i
            k=i+1
            while(j>=0 and k<n):
                if(s[j]!=s[k]):
                    break
                else:
                    if(k-j>ans[1]-ans[0]):
                        ans[0]=j
                        ans[1]=k
                j-=1
                k+=1
            j=i-1
            k=i+1
            while(j>=0 and k<n):
                if(s[j]!=s[k]):
                    break
                else:
                    if(k-j>ans[1]-ans[0]):
                        ans[0]=j
                        ans[1]=k
                j-=1
                k+=1
        return s[ans[0]:ans[1]+1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends