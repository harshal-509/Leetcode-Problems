#User function Template for python3
import bisect
def kthSmallest(mat, n, k): 
    # Your code goes here
    def hs(m):
        s=0
        for i in range(n):
            s+=bisect.bisect_right(mat[i],m)
        return s
    ans=0
    i=mat[0][0]
    j=mat[n-1][n-1]
    while(i<=j):
        mid=i+(j-i)//2
        if(hs(mid)<k):
            i=mid+1
        else:
            ans=mid
            j=mid-1
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends