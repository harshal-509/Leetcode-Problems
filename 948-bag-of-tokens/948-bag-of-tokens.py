class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans=0
        n=len(tokens)
        i=0
        j=n-1
        score=0
        while(i<=j):
            if(power>=tokens[i]):
                power-=tokens[i]
                score+=1
                i+=1
            else:
                if(score):
                    power+=tokens[j]
                    score-=1
                    j-=1
                else:
                    break
            ans=max(ans,score)
        return ans