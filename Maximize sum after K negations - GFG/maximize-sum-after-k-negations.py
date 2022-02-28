#User function Template for python3

class Solution:
    def maximizeSum(self, arr, p, k):
        # Your code goes here
        neg=[]
        pos=[]
        flag=0
        n=0
        m=0
        for i in range(p):
            if(arr[i]<0):
            	neg.append(arr[i])
            	m+=1
            elif(arr[i]>0):
                pos.append(arr[i])
                n+=1
            else:
                flag=1
        neg.sort()
        pos.sort()
        ans=0
        if(k<=m):
            for i in range(n):
                ans+=pos[i]
            for i in range(k):
                ans+=abs(neg[i])
            for i in range(k,m):
                ans+=neg[i]
        else:
            if(flag):
                for i in range(n):
                    ans+=pos[i]
                for i in range(m):
                    ans+=abs(neg[i])
            else:
                if((k-m)%2==0):
                    for i in range(n):
                        ans+=pos[i]
                    for i in range(m):
                        ans+=abs(neg[i])
                else:
                    for i in range(n):
                        ans+=pos[i]
                    for i in range(m):
                        ans+=abs(neg[i])
                    t=int(1e9)+1
                    if(pos):
                        t=pos[0]
                    if(neg):
                        t=min(t,abs(neg[-1]))
                    ans-=2*t
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maximizeSum(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends