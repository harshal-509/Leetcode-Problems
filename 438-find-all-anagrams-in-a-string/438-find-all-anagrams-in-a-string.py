class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        if(m>n):
            return []
        else:
            z=Counter(s[:m])
            ans=[]
            z1=Counter(p)
            i=0
            j=m
            while(i<n and j<=n):
                flag=0
                for k in z1:
                    if(z[k]!=z1[k]):
                        flag=1
                if(flag==0):
                    ans.append(i)
                z[s[i]]-=1
                if(j<n):
                    z[s[j]]+=1
                i+=1
                j+=1
            return ans