ans=[]
for i in range(1,9):
    x=i
    for j in range(i+1,10):
        x=x*10+j
        ans.append(x)
    ans.sort()
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s=[]
        for i in ans:
            if(i>=low and i<=high):
                s.append(i)
        return s