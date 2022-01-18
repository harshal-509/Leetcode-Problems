class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k=n
        n=len(flowerbed)
        x=flowerbed.count(1)
        ans=0
        if(x==0):
            if(n%2!=0):
                n+=1
            ans=n//2
        elif(x==1):
            m=flowerbed.index(1)
            ans+=m//2
            ans+=(n-m-1)//2
        else:
            a=-1
            b=-1
            ans=0
            for i in range(n):
                if(flowerbed[i]==1):
                    if(a==-1):
                        a=i
                    elif(b==-1):
                        b=i
                    else:
                        a=b
                        b=i
                    if(a!=-1 and b!=-1):
                        if((b-a-1)%2==0):
                            ans+=(b-a-2)//2
                        else:
                            ans+=(b-a-1)//2
                    elif(a!=-1 and b==-1):
                        ans+=a//2
            ans+=(n-b-1)//2
        return ans>=k