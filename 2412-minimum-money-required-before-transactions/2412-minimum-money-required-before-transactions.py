class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        ans=0
        s=0
        n=len(transactions)
        for i in range(n):
            s+=max(0,transactions[i][0]-transactions[i][1])
        for i in range(n):
            a=max(0,transactions[i][0]-transactions[i][1])
            ans=max(ans,s-a+transactions[i][0])
        return ans