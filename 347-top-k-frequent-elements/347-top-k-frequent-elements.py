class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in Counter(nums).most_common(k):
            ans.append(i[0])
        return ans