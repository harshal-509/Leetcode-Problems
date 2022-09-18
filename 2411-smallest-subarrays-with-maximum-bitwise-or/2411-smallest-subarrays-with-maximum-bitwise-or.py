class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # def inc(temp,val):
        #     s=bin(val)[2:]
        #     s="0"*(32-len(s))+s
        #     jtg=0
        #     for ip in range(32):
        #         if(s[ip]=='1'):
        #             temp[jtg]+=1
        #         jtg+=1
        # def dec(temp,val):
        #     s=bin(nums[i])[2:]
        #     s="0"*(32-len(s))+s
        #     jtg=0
        #     for ip in range(32):
        #         if(s[ip]=='1'):
        #             temp[jtg]-=1
        #         jtg+=1
        # def check(a,b):
        #     for i in range(32):
        #         if(a[i] and not(b[i]) or (b[i] and not(a[i]))):
        #             return 0
        #     return 1
        # ans=[]
        # s=0
        # n=len(nums)
        # arr=[0]*n
        # for i in range(n-1,-1,-1):
        #     s=s|nums[i]
        #     arr1=[0]*32
        #     inc(arr1,s)
        #     arr[i]=arr1
        # i=0
        # j=0
        # temp=[0]*32
        # while(i<n and j<n):
        #     x=check(temp,arr[i])
        #     if(x):
        #         ans.append(max(1,j-i))
        #         dec(temp,nums[i])
        #         i+=1
        #     else:
        #         inc(temp,nums[j])
        #         j+=1
        # while(i<n):
        #     x=check(temp,arr[i])
        #     if(x):
        #         ans.append(max(1,j-i))
        #         dec(temp,nums[i])
        #     i+=1
        # return ans
        
        
        n=len(nums)
        ans=[1 for i in range(n)]
        arr=[0 for i in range(30)]
        for i in range(n-1,-1,-1):
            a=1
            for j in range(0,30):
                if(nums[i]&(1<<j)):
                    arr[j]=i
                a=max(a,arr[j]-i+1)
            ans[i]=a
        return ans