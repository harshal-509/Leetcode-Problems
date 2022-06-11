#User function Template for python3

class Solution:
    def nullPoints(self, n, a, getAnswer):
        # Your code goes here 
        
        def search(l,h,a,n):
           mid = (l+h)/2
           d = 0
           for i in range(n):
               d += (1/(mid - a[i]))
           if abs(d)< 0.0000001:
               return mid
           if d > 0:
               return search(mid,h,a,n)
           else:
               return search(l,mid,a,n)
        for i in range(n-1):
           p = search(a[i],a[i+1],a,n)
           getAnswer[i] = p


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends