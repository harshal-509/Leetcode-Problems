class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0 for i in range(n)]
        for i in bookings:
            a=i[0]
            b=i[1]
            c=i[2]
            ans[a-1]+=c
            if(b<n):
                ans[b]-=c
        for i in range(1,n):
            ans[i]+=ans[i-1]
        return ans