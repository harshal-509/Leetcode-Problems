class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        a = 0
        ans = 0
        for i in properties:
            if(i[1]<a):
                ans+=1
            else:
                a=i[1]
        return ans