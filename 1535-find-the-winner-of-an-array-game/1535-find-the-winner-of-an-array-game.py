class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        arr=arr[::-1]
        t=0
        p=arr[-1]
        while(1):
            if(len(arr)==1):
                break
            x=arr[-2]
            y=arr[-1]
            if(x>y):
                arr.pop()
            else:
                arr[-1],arr[-2]=arr[-2],arr[-1]
                arr.pop()
            if(p==arr[-1]):
                t+=1
            else:
                p=arr[-1]
                t=1
            if(t==k):
                return arr[-1]
        return arr[0]