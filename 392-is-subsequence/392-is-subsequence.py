class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        ptr = 0
        
        for i in range(len(t)):
            if ptr < len(s) and s[ptr] == t[i]:
                ptr += 1
                
        return ptr == len(s)
