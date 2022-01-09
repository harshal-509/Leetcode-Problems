class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        dirx,diry=0,1
        for i in instructions:
            if i=="G":
                x,y=x+dirx,y+diry
            elif i=="L":
                dirx,diry=-1*diry,dirx
            else:
                dirx,diry=diry,-1*dirx
        return (x,y)==(0,0) or (dirx,diry)!=(0,1)