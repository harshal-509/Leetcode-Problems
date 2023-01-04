class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        z=Counter(tasks)
        ans=0
        for i in z:
            if(z[i]==1):
                return -1
            else:
                while(z[i]>1):
                    if(z[i]==2):
                        ans+=1
                        break
                    elif(z[i]==3):
                        ans+=1
                        break
                    elif(z[i]==4):
                        ans+=2
                        break
                    else:
                        ans+=1
                        z[i]-=3
        return ans