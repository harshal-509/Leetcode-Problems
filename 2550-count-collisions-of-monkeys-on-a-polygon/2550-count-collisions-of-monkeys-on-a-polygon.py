class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2,n,int(1e9+7))-2)%int(1e9+7)