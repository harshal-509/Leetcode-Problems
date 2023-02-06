class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        def check(x):
            if(x in ['a','e','i','o','u']):
                return 1
            return 0
        a=[0 for i in range(n)]
        for i in range(n):
            if(check(words[i][0]) and check(words[i][-1])):
                a[i]=1
        for i in range(1,n):
            a[i]+=a[i-1]
        ans=[]
        for i in queries:
            l=i[0]
            r=i[1]
            if(l==0):
                ans.append(a[r])
            else:
                ans.append(a[r]-a[l-1])
        return ans