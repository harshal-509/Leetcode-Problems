class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        n=len(pattern)
        for i in words:
            z=Counter([])
            flag=1
            for j in range(n):
                if(z[i[j]]):
                    if(z[i[j]]!=pattern[j]):
                        flag=0
                        break
                for k in z:
                    if(z[k]==pattern[j] and k!=i[j]):
                        flag=0
                        break
                z[i[j]]=pattern[j]
            if(flag):
                ans.append(i)
        return ans