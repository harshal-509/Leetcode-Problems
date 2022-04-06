class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n=len(arr)
        arr.sort()
        ans=0
        mod=1000000007
        for i in range(n):
            j=i+1
            k=n-1
            while(j<k):
                if(arr[i]+arr[j]+arr[k]==target):
                    x=1
                    y=1
                    while(j<k and arr[j]==arr[j+1]):
                        x+=1
                        j+=1
                    while(k>j and arr[k]==arr[k-1]):
                        y+=1
                        k-=1
                    if(arr[j]==arr[k]):
                        ans+=(((x%mod)*((x-1)%mod))%mod)//2
                        ans=ans%mod
                    else:
                        ans+=((x%mod)*(y%mod))%mod
                        ans=ans%mod
                    j+=1
                    k-=1
                elif(arr[i]+arr[j]+arr[k]<target):
                    j+=1
                else:
                    k-=1
        return ans