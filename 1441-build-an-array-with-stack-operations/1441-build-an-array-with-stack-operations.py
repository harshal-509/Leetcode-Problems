class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        x=1
        i=0
        ans=[]
        while(i<len(target)):
            if(target[i]==x):
                ans.append("Push")
                i+=1
                x+=1
            else:
                while(x<target[i]):
                    ans.append("Push")
                    ans.append("Pop")
                    x+=1
        return ans