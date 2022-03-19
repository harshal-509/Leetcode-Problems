class FreqStack:

    def __init__(self):
        self.cnt=collections.Counter()
        self.maxf=0
        self.stack=defaultdict(list)
    

    def push(self, val: int) -> None:
        cnt=self.cnt
        stack=self.stack
        cnt[val]+=1
        self.maxf=max(self.maxf,cnt[val])
        stack[cnt[val]].append(val)



    def pop(self) -> int:
        res=self.stack[self.maxf].pop()
        self.cnt[res]-=1
        if not self.stack[self.maxf]:
            self.maxf-=1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()