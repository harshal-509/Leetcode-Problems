class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=list(sentence.split())
        sentence.append(sentence[0])
        n=len(sentence)    
        for i in range(n-1):
            if(sentence[i][-1]!=sentence[i+1][0]):
                return 0
        return 1