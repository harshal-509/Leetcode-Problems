class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def solve(a,k,p):
            ans=0
            n=len(a)
            i=0
            c=0
            j=0
            while(i<n):
                if(a[i]==p):
                    c+=1
                else:
                    if(k):
                        k-=1
                        c+=1
                    else:
                        while(j<i):
                            if(a[j]!=p):
                                k+=1
                                break
                            j+=1
                        c=i-j
                        j+=1
                        if(a[i]!=p):
                            k-=1
                        ans=max(ans,c)
                ans=max(ans,c)
                i+=1
            ans=max(ans,c)
            return ans
        return max(solve(answerKey,k,'T'),solve(answerKey,k,'F'))