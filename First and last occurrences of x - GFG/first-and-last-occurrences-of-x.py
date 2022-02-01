#User function Template for python3
def find(arr,n,x):
    # code here
    i=0
    j=n-1
    ans=-1
    while(i<=j):
        m=i+(j-i)//2
        if(arr[m]<=x):
            if(arr[m]==x):
                ans=m
            i=m+1
        else:
            j=m-1
    i=0
    j=n-1
    ans1=-1
    while(i<=j):
        m=i+(j-i)//2
        if(arr[m]>=x):
            if(arr[m]==x):
                ans1=m
            j=m-1
        else:
            i=m+1
    return [ans1,ans]
#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends