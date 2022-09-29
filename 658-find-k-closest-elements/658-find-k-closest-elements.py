import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        y=bisect.bisect_left(arr,x)
        n=len(arr)
        if(y<n and arr[y]==x):
            ans=[arr[y]]
            i=1
            a=y-1
            b=y+1
        else:
            ans=[]
            i=0
            if(y==0):
                a=-1
                b=0
            elif(y==n):
                b=n
                a=n-1
            elif(y==n-1):
                a=y-1
                b=y
            else:
                if(abs(arr[y]-x)<=abs(arr[y+1]-x)):
                    if(abs(arr[y]-x)<abs(arr[y-1]-x)):
                        a=y
                        b=a+1
                    else:
                        a=y-1
                        b=a+1
                else:
                    a=y+1
                    b=a+1
        print(b)
        while(i<k):
            if(a>=0 and b<=n-1):
                if(abs(arr[a]-x)<abs(arr[b]-x)):
                    ans.insert(0,arr[a])
                    a-=1
                elif(abs(arr[a]-x)>abs(arr[b]-x)):
                    ans.append(arr[b])
                    b+=1
                else:
                    ans.insert(0,arr[a])
                    a-=1
            else:
                break
            i+=1
        if(a==-1 and i!=k):
            while(i<k):
                ans.append(arr[b])
                b+=1
                i+=1
        if(b==n and i!=k):
            while(i<k):
                ans.insert(0,arr[a])
                a-=1
                i+=1
        return (ans)                