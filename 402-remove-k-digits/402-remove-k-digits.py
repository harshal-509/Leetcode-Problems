class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return '0'
        
        def remove_first_leftside_maximum(rem: str) -> str:
            prev = float('-inf')
            for i in range(len(rem)-1):
                if prev <= int(rem[i]) and int(rem[i]) > int(rem[i+1]):
                    return (rem[:i] + rem[i+1:]).lstrip('0')
                prev = int(rem[i])
            return rem[:len(rem)-1]
        
        ans = num
        for _ in range(k):
            ans = remove_first_leftside_maximum(ans)
        return ans if ans else '0'