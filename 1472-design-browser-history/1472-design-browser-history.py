class BrowserHistory:

    def __init__(self, homepage: str):
        self.l=[homepage]
        self.i=0
        self.n=1
    
    def visit(self, url: str) -> None:
        self.l=self.l[:self.i+1]
        self.l.append(url)
        self.i+=1
        self.n=self.i+1

    def back(self, steps: int) -> str:
        self.i=max(0,self.i-steps)
        return self.l[self.i]

    def forward(self, steps: int) -> str:
        self.i=min(self.n-1,self.i+steps)
        return self.l[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)