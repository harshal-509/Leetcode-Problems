class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        z=Counter(ransomNote)
        z1=Counter(magazine)
        for i in z:
            if(z[i]>z1[i]):
                return 0
        return 1