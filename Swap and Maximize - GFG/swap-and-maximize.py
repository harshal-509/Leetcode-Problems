#User function Template for python3


def maxSum(arr,n):
    # code here
    ans=0
    arr.sort()
    arr1=[]
    i=0
    j=n-1
    flag=0
    while(i<=j):
        if(flag==0):
            arr1.append(arr[i])
            i+=1
            flag=1
        else:
            arr1.append(arr[j])
            j-=1
            flag=0
    for i in range(1,n):
        ans+=abs(arr1[i]-arr1[i-1])
    ans+=abs(arr1[-1]-arr[0])
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int,input().split()))
    ans=maxSum(arr,n)
    print(ans)

# } Driver Code Ends