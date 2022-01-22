#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    p=0
    for i in range(n):
        if(arr[i]<=k):
            p+=1
    s=0
    if(p==0):
        return 0
    for i in range(p):
        if(arr[i]>k):
            s+=1
    ans=s
    i=0
    j=p
    while(i<n):
        if(j>=n):
            break
        if(arr[j]>k):
            s+=1
        if(arr[i]>k):
            s-=1
        ans=min(ans,s)
        j+=1
        i+=1
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends