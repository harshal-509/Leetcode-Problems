class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        ans=""
        for x in words:
            if x+'#' not in ans:
                ans+=x+'#'
        return len(ans)