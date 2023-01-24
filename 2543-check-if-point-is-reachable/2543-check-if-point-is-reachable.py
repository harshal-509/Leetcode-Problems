class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        
#         q=deque([[targetX,targetY]])
#         s=set()
#         while(q):
#             x,y=q.pop()
#             if(x==1 and y==1):
#                 return 1
#             if((x,y) not in s):
#                 s.add((x,y))
#                 if(x%2==0):
#                     q.appendleft([x//2,y])
#                 if(y%2==0):
#                     q.appendleft([x,y//2])
#                 q.appendleft([x,y+x])
#                 q.appendleft([x+y,y])
#         return 0


        a=gcd(targetX,targetY)
        while(a%2==0):
            a=a//2
        return a==1