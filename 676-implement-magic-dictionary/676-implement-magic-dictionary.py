class MagicDictionary:

    def __init__(self):
        self.arr=[]
        self.l=[]
    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.arr.append(i)
            self.l.append(len(i))
    def search(self, searchWord: str) -> bool:
        x=len(searchWord)
        for i in range(len(self.l)):
            ans=0
            if(x==self.l[i]):
                for j in range(x):
                    if(searchWord[j]==self.arr[i][j]):
                        pass
                    else:
                        ans+=1
                if(ans==1):
                    return 1
        return 0

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)