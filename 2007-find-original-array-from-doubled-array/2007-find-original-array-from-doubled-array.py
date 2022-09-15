class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n=len(changed)
        if(n%2!=0):
            return []
        z=Counter(changed)
        changed=set(changed)
        changed=sorted(changed)
        flag=0
        b=0
        for i in changed:
            if(i==0):
                if(z[i]%2==0):
                    b=z[i]//2
                    z[i]=z[i]//2
                else:
                    flag=1
                    break
            elif(z[i*2]>0):
                b+=z[i]
                z[i*2]-=z[i]
                z[i]*=2
        a=0
        for i in z:
            if(i==0):
                a+=z[i]
            elif(z[i]>0):
                a+=z[i]//2
            elif(z[i]<0):
                flag=1
        if(a!=n//2 or flag or b!=n//2):
            return []
        else:
            ans=[]
            for i in z:
                if(i==0):
                    while(z[i]):
                        ans.append(i)
                        z[i]-=1
                if(z[i]>0):
                    for j in range(z[i]//2):
                        ans.append(i)
            return ans