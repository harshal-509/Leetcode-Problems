
def countRev (s):
    # your code here
    p=[]
    n=len(s)
    if(n%2):
        return -1
    ans=0
    for i in range(n):
        if(s[i]=="{"):
            p.append(s[i])
        else:
            if(p and p[-1]=="{"):
                p.pop()
            else:
                p.append("{")
                ans+=1
    return ans+len(p)//2
#{ 
#  Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends