class WordDictionary:

    def __init__(self):

        self.wordlist = []

        self.lengthlist = []

        

    def addWord(self, word: str) -> None:

        self.wordlist.append(word)

        self.lengthlist.append(len(word))

        

    def search(self, word: str) -> bool:

        def check(n):

            if len(n) != len(word):

                return False

            for i in range(len(word)):

                if word[i] == ".":

                    continue

                elif word[i] == n[i]:

                    continue

                else:

                    return False

            return True
        if len(word) not in self.lengthlist:

            return False

                

        if "." not in word:

            if word in self.wordlist:

                return True

            else:

                return False
        for j in self.wordlist:
            res=check(j)
            if(res):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)