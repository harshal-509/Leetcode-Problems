class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def pal(s):
            return s==s[::-1]
        ans=[]
        z1=Counter([])
        z=Counter([])
        n=len(words)
        for i in range(n):
            z[words[i][::-1]]=i+1
        for i in range(n):
            for j in range(len(words[i])+1):
                x=words[i][:j]
                y=words[i][j:]
                if(pal(x) and z[y] and not(z1[(z[y]-1,i)])):
                    if(z[y]-1!=i):
                        ans.append([z[y]-1,i])
                        z1[(z[y]-1,i)]+=1
                if(pal(y) and z[x] and not(z1[(i,z[x]-1)])):
                    if(z[x]-1!=i):
                        ans.append([i,z[x]-1])
                        z1[(i,z[x]-1)]+=1
        return ans