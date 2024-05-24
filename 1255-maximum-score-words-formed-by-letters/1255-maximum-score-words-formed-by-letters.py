class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def calc(s):
            ans=0
            for i in s:
                x = ord(i)-97
                ans+= score[x]
            return ans
        def possible(s):
            t=Counter(s)
            for i in t:
                if(t[i]<=z[i]):
                    pass
                else:
                    return 0
            return 1
        def solve(index,z):
            if(index>=n):
                return 0
            curr= words[index]
            a=0
            if(possible(curr)):
                for i in curr:
                    z[i]-=1
                a = solve(index+1,z) + calc(curr)
                for i in curr:
                    z[i]+=1
            b = solve(index+1,z)
            return max(a,b)
        z=Counter(letters)
        n=len(words)
        return solve(0,z)