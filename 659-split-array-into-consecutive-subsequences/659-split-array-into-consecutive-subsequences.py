class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        a=Counter([])
        z=Counter(nums)
        for i in nums:
            if(z[i]):
                if(a[i]):
                    a[i]-=1
                    z[i]-=1
                    a[i+1]+=1
                else:
                    if(z[i+1] and z[i+2]):
                        z[i]-=1
                        z[i+1]-=1
                        z[i+2]-=1
                        a[i+3]+=1
                    else:
                        return 0
        return 1