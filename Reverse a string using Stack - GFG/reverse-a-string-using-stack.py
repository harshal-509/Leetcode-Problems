#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    
    #Add code here
    s=[]
    n=len(S)
    for i in range(n):
        s.append(S[i])
    ans=""
    for i in range(n):
        ans+=s.pop()
    return ans
#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends