class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if(i.isnumeric() or (i>="a" and i<="z") or (i>="A" and i<="Z")):
                a+=i.lower()
        return a==a[::-1]