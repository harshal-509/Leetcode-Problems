class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        z=Counter(word1)
        z1=Counter(word2)
        for i in z:
            for j in z1:
                if(z1[j]==z[i]):
                    z1[j]=0
                    z[i]=0
                    break
            if(z[i]):
                return 0
        for i in z:
            if(i not in z1):
                return 0
        return 1