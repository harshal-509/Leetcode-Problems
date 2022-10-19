class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        z=Counter(words)
        t=z.most_common(k)
        ans=[]
        for i in t:
            ans.append(i[0])
        return ans