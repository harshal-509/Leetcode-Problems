class Solution:
    def maxScore(self, nums: List[int]) -> int:
        temp=[]
        temp1=[]
        for i in nums:
            if(i>=0):
                temp.append(i)
            else:
                temp1.append(i)
        temp.sort(reverse=True)
        temp1.sort(reverse=True)
        temp+=temp1
        for i in range(1,len(temp)):
            temp[i]+=temp[i-1]
        ans=0
        for i in temp:
            if(i>0):
                ans+=1
        return ans