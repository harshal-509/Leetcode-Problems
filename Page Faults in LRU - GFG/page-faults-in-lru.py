#User function Template for python3

class Solution:
    def pageFaults(self, n, c, pages):
        # code here
        page=[[-1,0] for i in range(c)]
        p=1
        ans=0
        for i in range(n):
            flag=0
            for j in range(c):
                if(page[j][0]==pages[i]):
                    flag=1
                    page[j][1]=p
                    p+=1
                    break
            if(flag):
                pass
            else:
                ans+=1
                flag=1
                for j in range(c):
                    if(page[j][0]==-1):
                        page[j][0]=pages[i]
                        page[j][1]=p
                        flag=0
                        p+=1
                        break
                if(flag):
                    t=1001
                    ind=-1
                    for j in range(c):
                        if(page[j][1]<t):
                            t=page[j][1]
                            ind=j
                    page[ind][0]=pages[i]
                    page[ind][1]=p
                    p+=1
        return ans            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))

# } Driver Code Ends