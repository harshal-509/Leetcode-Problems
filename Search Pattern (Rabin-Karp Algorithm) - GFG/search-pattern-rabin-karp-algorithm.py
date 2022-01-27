#User function Template for python3
class Solution:
    def search(self, patt, s):
        # code here
        n=len(s)
        m=len(patt)
        i=0
        j=m
        ans=[]
        while(j<=n):
            k=0
            p=i
            q=j
            while(p<q):
                if(s[p]!=patt[k]):
                    break
                p+=1
                k+=1
            if(p==q):
                ans.append(i+1)
            i+=1
            j+=1
        if(not(ans)):
            return [-1]
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends